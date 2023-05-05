from django.shortcuts import render
from .logic import historiaclinica_logic as vl
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def historiaclinica_view(request, pk):
    if request.method == 'GET':
        historiaclinica_dto = vl.get_historiaclinica(pk)
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json')

    if request.method == 'PUT':
        data = json.loads(request.body)
        estadoCivil = data.get("estadoCivil")
        direccion = data.get("direccion")
        antecedentesEnfermedades = data.get("antecedentesEnfermedades")
        motivoConsulta = data.get("motivoConsulta")
        ultimaModificacion = data.get("ultimaModificacion")
 
        historiaclinica_dto = vl.update_historiaclinica(pk, estadoCivil, direccion, antecedentesEnfermedades, motivoConsulta, ultimaModificacion)
        historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
        return HttpResponse(historiaclinica, 'application/json')

def historiasclinicas_view(request):
    if request.method == 'GET':
        
        historiaclinica_dto = vl.get_historiasclinicas()
        historiasclinicas = serializers.serialize('json', historiaclinica_dto,)
        return HttpResponse(historiasclinicas, 'application/json')


@csrf_exempt
def historiaclinica_view(request):
    
        if request.method == 'POST':
            historiaclinica_dto = vl.create_historiaclinica(json.loads(request.body))
            historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
            return HttpResponse(historiaclinica, 'application/json')

# Create your views here.


