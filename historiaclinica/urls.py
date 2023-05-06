from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('', views.historiasclinicas_view, name='historiaclinica_view'),
    path('<int:pk>', views.historiaclinica_view, name='historiaclinica_login'),
    path('historiaclinicaCreate/', csrf_exempt(views.create_historiaclinica), name='historiaclinicaCreate'),
]