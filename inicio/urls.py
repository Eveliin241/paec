from django.urls import path
from . import views

urlpatterns = [
    # Solo mantenemos la ruta raíz ('/') que llama a la vista 'home'.
    path('', views.home, name='home'),
    
    # Las rutas 'about/', 'servicios/', y 'contacto/' han sido eliminadas.
]