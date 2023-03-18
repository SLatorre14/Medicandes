from django.db import models

class HistoriaClinica(models.Model):
    numHistoriaClinica = models.IntegerField
    dni = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    edad = models.IntegerField
    ocupacion = models.CharField(max_length=50)
    fechaNacimiento = models.DateTimeField(auto_now_add=True)
    fechaCreacionHistoria = models.DateTimeField(auto_now_add=True)
    estadoCivil = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    antecedentesEnfermedades = models.CharField(max_length=50)
    motivoConsulta = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
# Create your models here.
