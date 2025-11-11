from django.shortcuts import render

def home(request):
    return render(request, 'inicio/home.html', {'titulo': 'PAEC - Inicio', 'mensaje': 'Bienvenido a PAEC!'})

def about(request):
    return render(request, 'inicio/about.html', {'titulo': 'PAEC - Acerca de', 'mensaje': 'Conoce más sobre PAEC.'})

def servicios(request):
    return render(request, 'inicio/servicios.html', {'titulo': 'PAEC - Servicios', 'mensaje': 'Estos son nuestros servicios.'})

def contacto(request):
    return render(request, 'inicio/contacto.html', {'titulo': 'PAEC - Contacto', 'mensaje': 'Contáctanos aquí.'})
