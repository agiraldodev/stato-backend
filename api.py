from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token

api = NinjaAPI(
    title="Stato API - Hospital Universitario San José",
    version="1.0.0",
    description="API para el área de estadística y analítica de datos",
)


# Este esquema es lo que React debe enviar obligatoriamente
class LoginRequestSchema(Schema):
    numCedula: str
    clave: str


@api.get("/auth/csrf", tags=["Autenticación"])
def get_csrf_token(request):
    """
    Nuxt debe llamar esto una vez al cargar la app para obtener la cookie csrftoken.
    """
    return {"csrftoken": get_token(request)}


# Endpoint tipo POST para el login
@api.post("/auth/login", tags=["Autenticación"])
def login_colaborador(request, data: LoginRequestSchema):
    """
    Endpoint para autenticar colaboradores mediante número de cédula y contraseña.
    Fase actual: Simulación local con la base de datos de Postgres.
    """
    # Pasamos los datos al backend personalizado en settings
    user = authenticate(request, username=data.numCedula, password=data.clave)

    if user is not None:
        # Si las credenciales son válidas, iniciamos la sesión en Django
        login(request, user)

        # Simulamos respuesta exitosa
        return {
            "status": "success",
            "message": "Autenticación exitosa",
            "colaborador": {
                "numCedula": user.username,
                "estado": "activo",
                "es_admin": user.is_superuser,
            },
        }
    else:
        # Si falla, devolvemos un 401 Unauthorized sin dar pistas de qué falló
        return JsonResponse(
            {
                "detail": "Número de cédula o contraseña incorrectos",
            },
            status=401,
        )
