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
    

# Create your views here.
