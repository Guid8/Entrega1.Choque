from django.urls import path
from .views import *

urlpatterns = [
    path('cursos/', cursos, name='cursos'),
    path('curso/', curso),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('', inicio, name='inicio'),
    path('entregables/', entregables, name='entregables'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('profeFormulario/', profeFormulario, name='profeFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar),
    
]
