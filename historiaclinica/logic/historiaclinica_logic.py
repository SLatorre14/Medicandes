from ..models import HistoriaClinica

def get_historiaclinica(numHistoriaClinica):
    historiaClinica = HistoriaClinica.objects.get(pk=numHistoriaClinica)
    return historiaClinica