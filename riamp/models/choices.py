from django.db import models


class EstadoConciencia(models.TextChoices):
    ALERTA = "ALERTA", "Alerta"
    NO_ALERTA = "NO ALERTA", "No Alerta"


class NivelRiesgo(models.TextChoices):
    NO_APLICA = "NO APLICA", "No Aplica"
    BAJO = "BAJO", "Bajo"
    ALTO = "ALTO", "Alto"
    RIESGO_NO_EVALUADO = "RIESGO NO EVALUADO", "Riesgo No Evaluado"


class DestinoMadre(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Destino Madre"
        verbose_name_plural = "Destinos Madre"

    def __str__(self):
        return self.nombre


class TipoTerminacionGestacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tipo Terminación Gestación"
        verbose_name_plural = "Tipos Terminación Gestación"

    def __str__(self):
        return self.nombre


class MetodoAnticonceptivo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Método Anticonceptivo"
        verbose_name_plural = "Métodos Anticonceptivos"

    def __str__(self):
        return self.nombre


class ObservacionAnticoncepcion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Observación Anticoncepción"
        verbose_name_plural = "Observaciones Anticoncepción"

    def __str__(self):
        return self.nombre


class ResultadoSifilis(models.TextChoices):
    POSITIVO = "POSITIVO", "Positivo"
    NEGATIVO = "NEGATIVO", "Negativo"
    RIESGO_NO_EVALUADO = "RIESGO NO EVALUADO", "Riesgo No Evaluado"
    NO_APLICA = "NO APLICA", "No Aplica"


class ResultadoVIH(models.TextChoices):
    REACTIVO = "REACTIVO", "Reactivo"
    NO_REACTIVO = "NO REACTIVO", "No Reactivo"
    RIESGO_NO_EVALUADO = "RIESGO NO EVALUADO", "Riesgo No Evaluado"
    NO_APLICA = "NO APLICA", "No Aplica"


class ResultadoTSH(models.TextChoices):
    NORMAL = "NORMAL", "Normal"
    ALTERADO = "ALTERADO", "Alterado"
    RIESGO_NO_EVALUADO = "RIESGO NO EVALUADO", "Riesgo No Evaluado"
    NO_APLICA = "NO APLICA", "No Aplica"


class NumeroNacidosVivos(models.IntegerChoices):
    NO_APLICA = 0, "No Aplica"
    UNO = 1, "1"
    DOS = 2, "2"
    TRES = 3, "3"
    CUATRO = 4, "4"


class ClasificacionPesoNacer(models.TextChoices):
    BAJO_PESO = "BAJO PESO AL NACER", "Bajo Peso al Nacer"
    RIESGO_BAJO_PESO = "EN RIESGO BAJO PESO", "En Riesgo Bajo Peso"
    PESO_ADECUADO = "PESO ADECUADO", "Peso Adecuado"
    MACROSOMICO = "MACROSÓMICO", "Macrosómico"
    REVISAR_PESO = "REVISAR PESO AL NACER", "Revisar Peso al Nacer"


class SiNoNoAplica(models.TextChoices):
    SI = "SI", "Sí"
    NO = "NO", "No"
    NO_APLICA = "NO APLICA", "No Aplica"
