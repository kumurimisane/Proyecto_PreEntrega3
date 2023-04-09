from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='index'),
    path('incripcion/', inscripcion, name='incripcion'),
    path('cursos/', cursos, name='cursos'),
    path('entergables/', entregables, name='entergables'),
    path('buscardor/', buscar, name="buscar")
]
