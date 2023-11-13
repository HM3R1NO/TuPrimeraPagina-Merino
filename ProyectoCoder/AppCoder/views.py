from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *
from django.http import HttpResponse

#Vistas Basadas en Clases (CVB)
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy


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

def profesorForm(request):
    if request.method == 'POST':
        miFormulario = ProfesorForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            data = Profesor(nombre = data['nombre'], apellido = data['apellido'], email = data['email'], edad = data['edad'])
            data.save()
            return render(request, 'AppCoder/index.html')
    else:
        miFormulario = ProfesorForm()
    return render(request, 'AppCoder/profesorForm.html', {"miFormulario":miFormulario})

#leer Profesores
def leerProfesores(request):
    profesores= Profesor.objects.all() 
    contexto={'profesores':profesores}
    return render(request, 'AppCoder/leerProfesores.html', contexto)

#eliminar profesores
def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    # vuelvo al menú
    profesores = Profesor.objects.all()  # trae todos los profesores
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

#editar profesores

def editarProfesor(request, profesor_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ProfesorForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.edad = informacion['edad']

            profesor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/index.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,'email': profesor.email, 'edad': profesor.edad})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarProfesores.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

#===============================================================

class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "AppCoder/curso_lista.html"


class CursoDetailView(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"


class CursoCreateView(CreateView):
    model = Curso
    template_name = "AppCoder/curso_crear.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada']


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "AppCoder/curso_editar.html"
    success_url = reverse_lazy('ListaCursos')
    fields = ['nombre', 'camada']

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "AppCoder/curso_borrar.html"
    success_url = reverse_lazy('ListaCursos')
    