from django.shortcuts import render
from .logic import adenda_logic as vl
from django.core import serializers
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def adenda_view(request, pk):
    if request.method == 'GET':
        adenda_dto = vl.get_adenda(pk)
        adenda = serializers.serialize('json', [adenda_dto,])
        return HttpResponse(adenda, 'application/json')
    
def adenda_view(request):
    if request.method == 'POST':
        adenda_dto = vl.create_adenda(json.loads(request.body))
        adenda = serializers.serialize('json', [adenda_dto,])
        return HttpResponse(adenda, 'application/json')
