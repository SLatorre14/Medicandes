from django.shortcuts import render
from .logic import historiaclinica_logic as vl
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from .forms import HistoriaClinicaForm
from .logic.historiaclinica_logic import create_historiaclinica
from django.contrib.auth.decorators import login_required
from medicandes.auth0backend import getRole

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
    role = getRole(request)
    if role == "Doctor" or role == "Administrador del sistema":
        if request.method == 'GET':
            
            historiaclinica_dto = vl.get_historiasclinicas()
            historiasclinicas = serializers.serialize('json', historiaclinica_dto,)
            return HttpResponse(historiasclinicas, 'application/json')
    else:
        return HttpResponse("Unauthorized User")

@csrf_exempt
def historiaclinica_view(request):
    
        if request.method == 'POST':
            historiaclinica_dto = vl.create_historiaclinica(json.loads(request.body))
            historiaclinica = serializers.serialize('json', [historiaclinica_dto,])
            return HttpResponse(historiaclinica, 'application/json')
        
        
@login_required
def historiaclinica_create(request):
    role = getRole(request)
    if role == "Doctor" or "Administrador del sistema":
        if request.method == 'POST':
            form = HistoriaClinicaForm(request.POST)
            if form.is_valid():
                create_historiaclinica(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created historia clinica')
                return HttpResponseRedirect(reverse('historiaclinicaCreate'))
            else:
                print(form.errors)
        else:
            form = HistoriaClinicaForm()

        context = {
            'form': form,
        }
        return render(request, 'Historiaclinica/historiaclinicaCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")




