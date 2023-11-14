from django.urls import path
from AppCoder.views import *

#Vistas Basadas en Clases (CVB)
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.views.generic import ListView

urlpatterns = [
    path('', inicio, name="home"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profe"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),
    path('curso/',curso,name='curso'),

    #url de formularios
    path("cursoForm/", cursoForm,name="cursoForm"),
    path("estudianteForm/",estudianteForm, name="estudianteForm"),
    path('profesorForm/', profesorForm, name='profesorForm'),
    path('leerProfesores/', leerProfesores, name='leerProfesores'),
    path("eliminarProfesor/<profesor_nombre>",eliminarProfesor, name='eliminarProfesor'),
    path("editarProfesores/<profesor_nombre>",editarProfesor, name='editarProfesor'),

    #Clases basadas en Vistas CVB

    path('cursos/lista/', CursoListView.as_view(), name = "ListaCursos"),
    path('cursos/nuevo/', CursoCreateView.as_view(), name = "NuevoCurso"),
    path('cursos/<pk>/', CursoDetailView.as_view(), name = "DetalleCurso"),
    path('cursos/<pk>/editar/', CursoUpdateView.as_view(), name = "EditarCurso"),
    path('cursos/<pk>/borrar/', CursoDeleteView.as_view(), name = "BorrarCurso"),

    #LogIn -Register -LogOut

    path('logIn/', login_view, name='LogIn'),
    path('singUp/', register, name='SingUp'),
    path('logOut/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='LogOut')


]