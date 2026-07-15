from django.db import models


class Paciente(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = "CC", "Cédula de Ciudadanía"
        CE = "CE", "Cédula de Extranjería"
        TI = "TI", "Tarjeta de Identidad"
        PE = "PE", "Permiso Especial de Permanencia"

    class Sexo(models.TextChoices):
        M = "M", "Masculino"
        F = "F", "Femenino"

    class Zona(models.TextChoices):
        RURAL = "R", "Rural"
        URBANA = "U", "Urbana"

    tipo_documento = models.CharField(
        max_length=2,
        choices=TipoDocumento.choices,
        null=True,
        blank=True,
    )
    numero_documento = models.CharField(max_length=20, unique=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=255, blank=True, null=True)
    zona = models.CharField(
        max_length=1,
        choices=Zona.choices,
        null=True,
        blank=True,
    )
    sexo = models.CharField(
        max_length=1,
        choices=Sexo.choices,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.numero_documento} {self.primer_apellido} {self.segundo_apellido or ''} {self.primer_nombre} {self.segundo_nombre or ''}".strip()

    # Función para guardar los apellidos y nombres del paciente en mayúsculas
    def save(self, *args, **kwargs):
        self.primer_nombre = self.primer_nombre.strip().upper()
        self.primer_apellido = self.primer_apellido.strip().upper()

        if self.segundo_nombre:
            self.segundo_nombre = self.segundo_nombre.strip().upper()

        if self.segundo_apellido:
            self.segundo_apellido = self.segundo_apellido.strip().upper()

        super().save(*args, **kwargs)
