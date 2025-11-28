from django.shortcuts import render


def contacto(request):
    return render(request, 'inicio/index.html')

def home(request):
    return render(request, 'inicio/home.html')

def about(request):
    return render(request, 'inicio/base.html')

def servicios(request):
    return render(request, 'inicio/servicios.html')

