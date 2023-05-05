from django.shortcuts import render
from .logic import doctor_logic as vl
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def doctor_view(request, pk):
    if request.method == 'GET':
        doctor_dto = vl.get_doctor(pk)
        doctor = serializers.serialize('json', [doctor_dto,])
        return HttpResponse(doctor, 'application/json')

def doctores_view(request):
    if request.method == 'GET':
        doctores = vl.get_doctores()
        doctores_dto = serializers.serialize('json', doctores)
        return HttpResponse(doctores_dto, 'application/json')



def doctor_view(request):
    if request.method == 'POST':
        doctor_dto = vl.create_doctor(json.loads(request.body))
        doctor = serializers.serialize('json', [doctor_dto,])
        return HttpResponse(doctor, 'application/json')
