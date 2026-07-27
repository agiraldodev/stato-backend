from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import logout as django_logout

from riamp.api import router as riamp_router

api = NinjaAPI(
    title="Stato API - Hospital Universitario San José",
    version="1.0.0",
    description="API para el área de estadística y analítica de datos",
)

api.add_router("/riamp", riamp_router)


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
    user = authenticate(request, username=data.numCedula, password=data.clave)

    if user is not None:
        # Las cuentas admin/staff son exclusivas del panel /admin/,
        # no deben poder autenticarse en la API de colaboradores.
        if user.is_superuser or user.is_staff:
            return JsonResponse(
                {"detail": "Número de cédula o contraseña incorrectos"},
                status=401,
            )

        login(request, user)

        return {
            "status": "success",
            "message": "Autenticación exitosa",
            "colaborador": {
                "numCedula": user.username,
                "nombreCompleto": user.first_name,
                "estado": "activo",
                "es_admin": user.is_superuser,
                "grupos": list(user.groups.values_list("name", flat=True)),
                "permisos": list(user.get_all_permissions()),
            },
        }
    else:
        return JsonResponse(
            {"detail": "Número de cédula o contraseña incorrectos"},
            status=401,
        )

@api.get("/auth/me", tags=["Autenticación"])
def get_current_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "No hay sesión activa"}, status=401)

    # Misma restricción: una sesión de /admin/ no debe "colarse" como
    # sesión válida de colaborador en la API.
    if request.user.is_superuser or request.user.is_staff:
        return JsonResponse({"detail": "No hay sesión activa"}, status=401)

    return {
        "status": "success",
        "colaborador": {
            "numCedula": request.user.username,
            "nombreCompleto": request.user.first_name,
            "estado": "activo",
            "es_admin": request.user.is_superuser,
            "grupos": list(request.user.groups.values_list("name", flat=True)),
            "permisos": list(request.user.get_all_permissions()),
        },
    }
@api.post("/auth/logout", tags=["Autenticación"])
def logout_colaborador(request):
    """
    Cierra sesión del usuario actual. Invalida la cookie de sesión del lado del servidor (borra registro en tabla django_session)
    """
    django_logout(request)
    return {"status": "success", "message": "Sesión cerrada correctamente"}
