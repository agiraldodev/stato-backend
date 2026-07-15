from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from shared.models import Paciente, Municipio, Eapb, CIE10
from .choices import (
    EstadoConciencia,
    NivelRiesgo,
    DestinoMadre,
    TipoTerminacionGestacion,
    MetodoAnticonceptivo,
    ObservacionAnticoncepcion,
    ResultadoSifilis,
    ResultadoVIH,
)


class Evento(models.Model):
    fecha_evento = models.DateField(blank=True, null=True)
    hora_evento = models.TimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(
        Paciente, on_delete=models.PROTECT, related_name="eventos"
    )
    municipio = models.ForeignKey(
        Municipio, on_delete=models.PROTECT, related_name="eventos"
    )
    eapb = models.ForeignKey(
        Eapb, on_delete=models.PROTECT, related_name="eventos", null=True, blank=True
    )
    cie10 = models.ForeignKey(
        CIE10, on_delete=models.PROTECT, related_name="eventos", null=True, blank=True
    )

    estado_conciencia = models.CharField(
        max_length=10,
        choices=EstadoConciencia.choices,
        null=True,
        blank=True,
    )

    clasificacion_riesgo_gestacional = models.CharField(
        max_length=25,
        choices=NivelRiesgo.choices,
        null=True,
        blank=True,
    )

    clasificacion_riesgo_preeclampsia = models.CharField(
        max_length=25,
        choices=NivelRiesgo.choices,
        null=True,
        blank=True,
    )

    diagnostico_ingreso = models.TextField(blank=True, null=True)

    destino_madre = models.ForeignKey(
        DestinoMadre,
        on_delete=models.PROTECT,
        related_name="eventos",
        null=True,
        blank=True,
    )

    fecha_terminacion_gestacion = models.DateField(blank=True, null=True)

    tipo_terminacion_gestacion = models.ForeignKey(
        TipoTerminacionGestacion,
        on_delete=models.PROTECT,
        related_name="eventos",
        null=True,
        blank=True,
    )

    metodo_anticonceptivo = models.ForeignKey(
        MetodoAnticonceptivo,
        on_delete=models.PROTECT,
        related_name="eventos",
        null=True,
        blank=True,
    )

    fecha_suministro_metodo_anticonceptivo = models.DateField(blank=True, null=True)

    observacion_anticoncepcion = models.ForeignKey(
        ObservacionAnticoncepcion,
        on_delete=models.PROTECT,
        related_name="eventos",
        null=True,
        blank=True,
    )

    tamizaje_sifilis = models.CharField(
        max_length=25,
        choices=ResultadoSifilis.choices,
        null=True,
        blank=True,
        verbose_name="TAMIZAJE PARA SÍFILIS SEGÚN GPC SÍFILIS HOSPITALARIA",
    )
    fecha_resultado_pr_sifilis = models.DateField(blank=True, null=True)

    tamizaje_vih = models.CharField(
        max_length=25,
        choices=ResultadoVIH.choices,
        null=True,
        blank=True,
        verbose_name="TAMIZAJE  PARA VIH INTRAPARTO SEGÚN GPC",
    )
    fecha_resultado_vih = models.DateField(blank=True, null=True)
    fecha_lactancia_materna = models.DateField(
        blank=True,
        null=True,
        verbose_name="FECHA DE ATENCIÓN EN SALUD PARA LA PROMOCIÓN Y APOYO DE LA LACTANCIA MATERNA",
    )

    numero_nacidos_vivos = models.PositiveSmallIntegerField(
        verbose_name="REGISTRE EL NÚMERO DE RECIÉN NACIDOS VIVOS",
        validators=[MinValueValidator(1), MaxValueValidator(4)],
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Evento {self.id} - Paciente {self.paciente.numero_documento}"
