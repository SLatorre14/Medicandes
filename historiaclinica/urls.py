from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.historiaclinica_view, name='historiaclinica_login'),
    path('<numHistoriaClinica>', views.historiaclinica_view, name='historiaclinica_login')
]