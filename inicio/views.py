from django.shortcuts import render

def home(request):
    return render(request, 'inicio/home.html')

def about(request):
    return render(request, 'inicio/about.html')

def servicios(request):
    return render(request, 'inicio/servicios.html')

def contacto(request):
    return render(request, 'inicio/contacto.html')
