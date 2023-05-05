from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.historiasclinicas_view, name='historiaclinica_view'),
    path('<int:pk>', views.historiaclinica_view, name='historiaclinica_login')
]