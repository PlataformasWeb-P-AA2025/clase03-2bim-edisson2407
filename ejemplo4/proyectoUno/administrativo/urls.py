"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        # estudiantes
    path('estudiante/<int:id>', views.obtener_estudiante, 
         name='obtener_estudiante'),
    path('estudiante/crear', views.crear_estudiante, 
         name='crear_estudiante'),
    path('estudiante/<int:id>/editar', views.editar_estudiante, 
         name='editar_estudiante'),
    path('estudiante/<int:id>/eliminar', views.eliminar_estudiante, 
         name='eliminar_estudiante'),
    
    # paises
    path('pais/<int:id>', views.obtener_pais, name='obtener_pais'),
    path('pais/crear', views.crear_pais, name='crear_pais'),
    path('pais/<int:id>/editar', views.editar_pais, name='editar_pais'),
    path('pais/<int:id>/eliminar', views.eliminar_pais, name='eliminar_pais'),
 ]
