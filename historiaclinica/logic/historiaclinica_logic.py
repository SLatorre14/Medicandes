from ..models import HistoriaClinica

def get_historiaclinica(numHistoriaClinica):
    historiaClinica = HistoriaClinica.objects.get(pk=numHistoriaClinica)
    return historiaClinica

def create_historiaclinica(hist):
    historiaClinica = HistoriaClinica(name=hist["numHistoriaClinica"])
    historiaClinica.save()
    return historiaClinica