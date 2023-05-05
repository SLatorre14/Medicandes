from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.adendas_view, name='adendas_view'),
    path('<int:pk>', views.adenda_view, name='adenda_view')
]