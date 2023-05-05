from django.http import HttpResponse


def healthCheck(request):
        return HttpResponse('ok')


def home(request):
    return HttpResponse("Bienvenido a Medicandes")