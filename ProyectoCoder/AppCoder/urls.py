from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profe"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('curso/',curso,name='curso'),

    #url de formularios
    path("cursoForm/", cursoForm,name="cursoForm"),
]