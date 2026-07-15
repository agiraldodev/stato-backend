from django.contrib import admin

from .models import (
    Evento,
    DestinoMadre,
    TipoTerminacionGestacion,
    MetodoAnticonceptivo,
    ObservacionAnticoncepcion,
    Neonato,
)


class NeonatoInline(admin.TabularInline):
    model = Neonato
    extra = 1  # cuántas filas vacías mostrar por defecto para agregar
    fields = ("sexo", "peso", "talla", "edad_gestacional_rn")


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("fecha_evento", "fecha_registro", "paciente", "municipio", "eapb")
    search_fields = ("paciente__numero_documento", "municipio__nombre")
    list_filter = ("fecha_evento", "municipio")
    ordering = ("-fecha_evento",)
    inlines = [NeonatoInline]


@admin.register(DestinoMadre)
class DestinoMadreAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)
    ordering = ("nombre",)


@admin.register(TipoTerminacionGestacion)
class TipoTerminacionGestacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)
    ordering = ("nombre",)


@admin.register(MetodoAnticonceptivo)
class MetodoAnticonceptivoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)
    ordering = ("nombre",)


@admin.register(ObservacionAnticoncepcion)
class ObservacionAnticoncepcionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)
    ordering = ("nombre",)


@admin.register(Neonato)
class NeonatoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "evento",
        "sexo",
        "peso",
        "talla",
        "edad_gestacional_rn",
        "imc",
        "clasificacion_peso_nacer",
    )
    list_filter = ("sexo",)
    ordering = ("-fecha_registro",)
    readonly_fields = ("imc", "clasificacion_peso_nacer")
