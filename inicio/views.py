from django.shortcuts import render

def home(request):
    # CRÍTICO: Apuntamos al nombre real de tu archivo de plantilla, 'index.html'.
    return render(request, 'inicio/index.html') 

# Las funciones about, servicios, y contacto deben ser eliminadas de este archivo.