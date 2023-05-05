from ..models import HistoriaClinica

def get_historiaclinica(numHistoriaClinica):
    historiaClinica = HistoriaClinica.objects.get(pk=numHistoriaClinica)
    return historiaClinica

def get_historiasclinicas():
    historias = HistoriaClinica.objects.all()
    return historias

def create_historiaclinica(hist):
    historiaClinica = HistoriaClinica(name=hist["numHistoriaClinica"])
    historiaClinica.save()
    return historiaClinica

def update_historiaclinica(numHistoriaClinica, estadoCivil, direccion, antecedentesEnfermedades, motivoConsulta, ultimaModificacion):
    historiaClinica = get_historiaclinica(numHistoriaClinica)
    historiaClinica.estadoCivil = estadoCivil["estadoCivil"]
    historiaClinica.direccion = direccion["direccion"]
    historiaClinica.antecedentesEnfermedades = antecedentesEnfermedades["antecedentesEnfermedades"]
    historiaClinica.motivoConsulta = motivoConsulta["motivoConsulta"]
    historiaClinica.ultimaModificacion = ultimaModificacion["ultimaModificacion"]
    historiaClinica.save()
    return historiaClinica
