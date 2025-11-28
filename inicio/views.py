from django.shortcuts import render

def home(request):
    return render(request, 'inicio/index.html')  # asegúrate que sea index.html
