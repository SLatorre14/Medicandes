from django.db import models


class Doctor(models.Model):
    identificacion = models.FloatField(null=False, blank=True, default=None)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.identificacion)

# Create your models here.
