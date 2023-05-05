from django.contrib import admin 
from django.urls import path
from . import views
urlpatterns = [
    path('', views.doctores_view, name='doctores_view')
]