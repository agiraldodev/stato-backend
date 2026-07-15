from django.db import models


class Eapb(models.Model):
    codigo = models.CharField(max_length=20, null=True, blank=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "EAPB"
        verbose_name_plural = "EAPB"

    def __str__(self):
        return f"{self.nombre}"
