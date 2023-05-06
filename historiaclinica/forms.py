from django import forms
from .models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            'numHistoriaClinica', 
            'dni', 
            'apellidos', 
            'nombres', 
            'edad', 
            'ocupacion',
            'fechaNacimiento',
            'fechaCreacionHistoria',
            'estadoCivil', 
            'direccion', 
            'antecedentesEnfermedades', 
            'doctor',
        ]
        labels = {
            'numHistoriaClinica':'NumHistoriaClinica' , 
            'dni': 'Dni', 
            'apellidos': 'Apellidos', 
            'nombres': 'Nombres', 
            'edad':'Edad', 
            'ocupacion':'Ocupacion',
            'fechaNacimiento':'FechaNacimiento',
            'fechaCreacionHistoria':'FechaCreacionHistoria',
            'estadoCivil':'EstadoCivil', 
            'direccion':'Direccion', 
            'antecedentesEnfermedades':'AntecedentesEnfermeades', 
            'doctor':'Doctor',
        }