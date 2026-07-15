from django.db import models

class Departamento(models.Model):
    codigo = models.CharField(max_length=2, unique=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f"{self.nombre}"