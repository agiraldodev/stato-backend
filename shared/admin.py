# backend/shared/admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Departamento, Municipio, Eapb, CIE10, Paciente
from .resources import (
    DepartamentoResource,
    MunicipioResource,
    EapbResource,
    CIE10Resource,
)


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        "numero_documento",
        "primer_apellido",
        "segundo_apellido",
        "primer_nombre",
        "segundo_nombre",
        "fecha_nacimiento",
        "sexo",
    )
    list_display_links = ("numero_documento",)
    search_fields = (
        "numero_documento",
        "primer_apellido",
        "segundo_apellido",
        "primer_nombre",
        "segundo_nombre",
    )
    list_filter = ("tipo_documento", "sexo")
    ordering = (
        "primer_apellido",
        "segundo_apellido",
        "primer_nombre",
        "segundo_nombre",
    )


@admin.register(CIE10)
class CIE10Admin(ImportExportModelAdmin):
    resource_classes = [CIE10Resource]
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")
    ordering = ("codigo",)


@admin.register(Departamento)
class DepartamentoAdmin(ImportExportModelAdmin):
    resource_classes = [DepartamentoResource]
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")
    ordering = ("nombre",)


@admin.register(Municipio)
class MunicipioAdmin(ImportExportModelAdmin):
    resource_classes = [MunicipioResource]
    list_display = ("codigo", "nombre", "departamento")
    search_fields = ("codigo", "nombre")
    list_filter = ("departamento",)
    ordering = ("nombre",)


@admin.register(Eapb)
class EapbAdmin(ImportExportModelAdmin):
    resource_classes = [EapbResource]
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")
    ordering = ("nombre",)


admin.site.site_header = "Administración de Stato - HUSJ"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenid@"
