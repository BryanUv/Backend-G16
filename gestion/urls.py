# aca estaran declaradas todas las rutas relacionadas a la aplicacion de gestion
from django.urls import path
from .views import mostrarRecetas, vistaPrueba, controladorInicial, PlatosController, PlatoController	

urlpatterns = [
  path('prueba/', view=vistaPrueba),
  path('mostrar-recetas/', view=mostrarRecetas),
  path('prueba-drf/', view=controladorInicial),
  path('platos/', view=PlatosController.as_view()),
  path('plato/<int:id>', view=PlatoController.as_view())
]