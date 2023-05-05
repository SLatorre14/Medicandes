from ..models import Adenda

def get_adenda(numAdenda):
    adenda = Adenda.objects.get(pk=numAdenda)
    return adenda

def create_adenda(hist):
    adenda = Adenda(name=hist["numAdenda"])
    adenda.save()
    return adenda

def get_adendas():
    adendas = Adenda.objects.all()
    return adendas