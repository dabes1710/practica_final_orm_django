from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_laboratorios, name='listar_laboratorios'),
    path('crear/', views.crear_laboratorio, name='crear_laboratorio'),
    path('editar/<int:laboratorio_id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:laboratorio_id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
