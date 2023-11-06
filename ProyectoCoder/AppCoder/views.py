from django.shortcuts import render
from AppCoder.models import Curso, Estudiante
from AppCoder.forms import EstudianteForm
from django.http import HttpResponse

# Create your views here.
def curso(self):
    curso = Curso(nombre="Python", camada=55555)
    curso.save()
    documentoDeTexto = f"----->Curso {curso.nombre} Camada {curso.camada}" 
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return HttpResponse('vista profesores')

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return HttpResponse('vista entregables')

def cursoForm(request):
    if request.method == "POST":
        curso=Curso(nombre=request.POST["nombre"], camada=request.POST["camada"]) #En la clase al profe le falto asignar las variables(nombre=...,camada=...) y por eso daba error.
        curso.save()
        return render(request, "AppCoder/index.html")
    return render(request, "AppCoder/cursoForm.html")

# def cursoForm(request):
#     if request.method == "POST":
#         print(request.POST)  # Imprimir todo el diccionario request.POST
#         nombre = request.POST.get("nombre")  # Obtener el valor de "nombre"
#         camada = request.POST.get("camada")  # Obtener el valor de "camada"
#         print(f"Nombre: {nombre}, Camada: {camada}")  # Imprimir los valores específicos
#         curso = Curso(nombre=nombre, camada=camada)
#         curso.save()
#         return render(request, "AppCoder/index.html")
#     return render(request, "AppCoder/cursoForm.html")

def estudianteForm(request):
    if request.method == "POST":
        miFormulario = EstudianteForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            info=Estudiante(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            info.save()
            return render(request, "AppCoder/index.html")
    else:
        miFormulario=EstudianteForm()
    return render (request, "AppCoder/estudianteForm.html",{"miFormulario":miFormulario})

        