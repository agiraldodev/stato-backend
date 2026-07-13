from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class HospitalAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        En producción, 'username' será el número de cédula enviado desde el frontend.
        """
        if username is None:
            return None

        # MODO SIMULACIÓN (FASE ACTUAL): Validamos contra la DB local de Django

        try:
            # Buscar colaborador por su número de cédula (guardado en username)
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

        # ACTIVAR ESTO CUANDO LA API DE DINÁMICA ESTÉ LISTA Y TE LA HAYAN ENTREGADO
        import requests
        try:
            response = requests.post(
                "https://api-intranet.hospital.local/auth/login",
                json={"numCedula": username, "clave": password},
                timeout=5
            )
            if response.status_code == 200:
                # Si la API responde que es válido. Buscamos o creamos el usuario en Django
                user, created = User.objects.get_or_create(username=username)
                return user
        except requests.exceptions.RequestException:
            return None