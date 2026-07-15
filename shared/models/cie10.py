from django.db import models

class CIE10(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.TextField()

    class Meta:
        ordering = ["codigo"]
        verbose_name = "CIE10"
        verbose_name_plural = "CIE10"

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"