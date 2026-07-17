from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from .evento import Evento
from .choices import (
    ClasificacionPesoNacer,
    SiNoNoAplica,
    ResultadoTamizaje,
    ResultadoTamizajeAuditivo,
    EstadoSalidaRecienNacido,
)


class Neonato(models.Model):
    class Sexo(models.TextChoices):
        M = "M", "Masculino"
        F = "F", "Femenino"

    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name="neonatos"
    )

    num_certificado_nacimiento = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name="Número de certificado de nacimiento",
    )

    sexo = models.CharField(
        max_length=1,
        choices=Sexo.choices,
        null=True,
        blank=True,
    )

    peso = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(200), MaxValueValidator(6000)],
        verbose_name="Peso al nacer (gramos)",
    )

    talla = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(30), MaxValueValidator(60)],
        verbose_name="Talla al nacer (cm)",
    )

    edad_gestacional_rn = models.PositiveSmallIntegerField(
        verbose_name="REGISTRE LA EDAD GESTACIONAL EN SEMANAS DEL RECIÉN NACIDO POR CAPURRO Y/O BALLARD",
        validators=[MinValueValidator(20), MaxValueValidator(45)],
        null=True,
        blank=True,
    )

    imc = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False,
        verbose_name="IMC",
        help_text="Calculado automáticamente a partir de peso y talla.",
    )

    clasificacion_peso_nacer = models.CharField(
        max_length=30,
        choices=ClasificacionPesoNacer.choices,
        null=True,
        blank=True,
        verbose_name="Clasificación del peso al nacer",
        editable=False,
    )

    aplicacion_vitamina_k = models.CharField(
        max_length=10,
        choices=SiNoNoAplica.choices,
        null=True,
        blank=True,
        verbose_name="APLICACIÓN DE VITAMINA K",
    )

    fecha_vacunacion_hepatitis_b = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE VACUNACIÓN HEPATITIS B",
    )

    fecha_vacunacion_bcg = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE VACUNACIÓN BCG",
    )

    fecha_tsh_rn = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TOMA DE MUESTRA PARA TSH RN",
    )

    resultado_tsh_rn = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TSH RN",
    )

    fecha_reporte_tsh_rn = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE REPORTE DE RESULTADO TSH RN",
    )

    resultado_tamizaje_cardiopatia = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE CARDIOPATÍA",
    )

    fecha_tamizaje_cardiopatia = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE CARDIOPATÍA",
    )

    resultado_tamizaje_auditivo = models.CharField(
        max_length=25,
        choices=ResultadoTamizajeAuditivo.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE AUDITIVO",
    )

    fecha_tamizaje_auditivo = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE AUDITIVO",
    )

    resultado_tamizaje_hiperplasia_suprarrenal = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE HIPERPLASIA SUPRARRENAL",
    )

    fecha_tamizaje_hiperplasia_suprarrenal = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE HIPERPLASIA SUPRARRENAL",
    )

    resultado_tamizaje_hemoglobinopatias = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE HEMOGLOBINOPATÍAS",
    )

    fecha_tamizaje_hemoglobinopatias = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE HEMOGLOBINOPATÍAS",
    )

    resultado_tamizaje_galactosemia = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE GALACTOSEMIA",
    )

    fecha_tamizaje_galactosemia = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE GALACTOSEMIA",
    )

    resultado_tamizaje_fenilcetonuria = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE FENILCETONURIA",
    )

    fecha_tamizaje_fenilcetonuria = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE FENILCETONURIA",
    )

    resultado_tamizaje_fibrosis_quistica = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE FIBROSIS QUÍSTICA",
    )

    fecha_tamizaje_fibrosis_quistica = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE FIBROSIS QUÍSTICA",
    )

    resultado_tamizaje_deficiencia_biotinidasa = models.CharField(
        max_length=25,
        choices=ResultadoTamizaje.choices,
        null=True,
        blank=True,
        verbose_name="RESULTADO TAMIZAJE DEFICIENCIA DE BIOTINIDASA",
    )

    fecha_tamizaje_deficiencia_biotinidasa = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE TAMIZAJE DEFICIENCIA DE BIOTINIDASA",
    )

    fecha_egreso_recien_nacido = models.DateField(
        null=True,
        blank=True,
        verbose_name="FECHA DE EGRESO DEL RECIÉN NACIDO",
    )

    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Neonato"
        verbose_name_plural = "Neonatos"

    def _calcular_imc(self):
        if self.peso and self.talla:
            peso_kg = self.peso / 1000
            talla_m = self.talla / 100
            return round(peso_kg / (talla_m**2), 2)
        return None

    def _clasificar_peso_nacer(self):
        if self.peso is None:
            return None
        if 200 <= self.peso < 2500:
            return ClasificacionPesoNacer.BAJO_PESO
        if 2500 <= self.peso < 3000:
            return ClasificacionPesoNacer.RIESGO_BAJO_PESO
        if 3000 <= self.peso < 4000:
            return ClasificacionPesoNacer.PESO_ADECUADO
        if 4000 <= self.peso < 6000:
            return ClasificacionPesoNacer.MACROSOMICO
        return ClasificacionPesoNacer.REVISAR_PESO

    def save(self, *args, **kwargs):
        self.imc = self._calcular_imc()
        self.clasificacion_peso_nacer = self._clasificar_peso_nacer()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Neonato {self.id} - Evento {self.evento.id}"
