from django.db import models
from historiaclinica.models import HistoriaClinica

# Create your models here.
class Adenda(models.Model):
    numAdenda = models.FloatField(null=False, blank=True, default=None)
    fechaConsulta= models.DateTimeField(auto_now_add=True)
    motivoConsulta = models.CharField(max_length=50)
    HistoriaClinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, default= None)

    def __str__(self):
        return '{}'.format(self.numAdenda)