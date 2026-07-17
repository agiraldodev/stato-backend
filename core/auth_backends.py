from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from decouple import config
import jwt as pyjwt
import requests
import logging

User = get_user_model()
logger = logging.getLogger(__name__)


class HospitalAuthBackend(ModelBackend):
    """
    Autentica contra la API del hospital usando número de cédula (username) y clave.

    Excepción: usuarios marcados como is_superuser o is_staff se autentican
    localmente con su password de Django (para no depender de la API externa
    en caso de caída, y para poder entrar al /admin).
    """

    HOSPITAL_LOGIN_URL = config(
        "HOSPITAL_LOGIN_URL",
        default="http://soluciones.local/api-auth/auth/login",
    )

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        # --- Excepción: cuentas admin/staff usan password local de Django ---
        try:
            local_user = User.objects.get(username=username)
            if local_user.is_superuser or local_user.is_staff:
                if local_user.check_password(password):
                    return local_user
                return None  # es cuenta admin pero password incorrecto -> no seguir a la API
        except User.DoesNotExist:
            pass  # no existe localmente todavía, puede ser un colaborador nuevo -> seguir a la API

        # --- Autenticación real contra la API del hospital ---
        try:
            response = requests.post(
                self.HOSPITAL_LOGIN_URL,
                json={"username": username, "password": password},
                timeout=5,
            )
        except requests.exceptions.RequestException:
            logger.warning("No se pudo contactar la API del hospital")
            return None

        if response.status_code != 200:
            return None

        data = response.json()
        access_token = data.get("jwt")

        if not access_token:
            logger.error("La API del hospital respondió 200 pero sin campo 'jwt'")
            return None

        full_name, authorities = self._extract_claims(access_token)

        # Buscamos o creamos el usuario local, sincronizando el nombre
        user, created = User.objects.get_or_create(
            username=username,
            defaults={"first_name": full_name or ""},
        )

        # Si ya existía pero el nombre cambió en el hospital, lo actualizamos
        if not created and full_name and user.first_name != full_name:
            user.first_name = full_name
            user.save(update_fields=["first_name"])

        # IMPORTANTE: nunca guardamos ni verificamos el password local para
        # colaboradores del hospital. La API es la única fuente de verdad.
        if user.has_usable_password():
            user.set_unusable_password()
            user.save(update_fields=["password"])

        return user

    def _extract_claims(self, token):
        """
        El JWT del hospital viene firmado (no encriptado): se puede leer el
        payload sin necesidad de la clave secreta, ya que no estamos
        verificando la firma, solo extrayendo datos no sensibles.

        Campos confirmados en el payload real:
          - sub: número de cédula
          - authorities: rol del colaborador (ej. "ROLE_ADMINISTRADOR")
          - name_user: nombre completo
          - iat / exp: emisión / expiración
        """
        try:
            payload = pyjwt.decode(token, options={"verify_signature": False})
        except pyjwt.PyJWTError:
            logger.error("No se pudo decodificar el JWT del hospital")
            return None, None

        full_name = payload.get("name_user")
        authorities = payload.get("authorities")
        return full_name, authorities
