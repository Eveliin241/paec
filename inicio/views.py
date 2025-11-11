from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'titulo': 'Bienvenido a PAEC', 'mensaje': 'Aprendizaje y renovación para todos.'})

def servicios(request):
    return render(request, 'servicios.html', {'titulo': 'Nuestros Servicios'})

def contacto(request):
    return render(request, 'contacto.html', {'titulo': 'Contacto'})

def about(request):
    return render(request, 'about.html', {'titulo': 'Acerca de Nosotros'})

