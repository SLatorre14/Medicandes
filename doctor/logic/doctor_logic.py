from ..models import Doctor

def get_doctores():
    doctores = Doctor.objects.all()
    return doctores 

def get_doctor(identificacion):
    doctor = doctor.objects.get(pk=identificacion)
    return doctor

def create_doctor(hist):
    doctor = Doctor(name=hist["identificacion"])
    doctor.save()
    return doctor

