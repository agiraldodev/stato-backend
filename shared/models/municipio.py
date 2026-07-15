from django.db import models
from .departamento import Departamento

class Municipio(models.Model):
    codigo = models.CharField(max_length=5, unique=True)
    nombre = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='municipios')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f"{self.nombre}"