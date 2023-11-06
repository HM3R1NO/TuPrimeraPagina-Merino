from django.urls import path
from AppCoder.views import *
urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores, name="profe"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables),
    path('curso/',curso,name='curso'),
]