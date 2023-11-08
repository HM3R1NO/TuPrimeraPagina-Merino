from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import *
 
# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/index.html')

def aficionadoForm(request):
    if request.method == 'POST':
        miFormulario = AficionadoForm(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Aficionado(nombre = info['nombre'], apellido = info['apellido'], edad = info['edad'])
            info.save()
            return render(request, 'AppCoder/index.html')
    else:
        miFormulario = AficionadoForm()
    return render(request, "AppCoder/aficionadoForm.html",{'miFormulario':miFormulario})

def aventureroForm(request):
    if request.method == 'POST':
        miFormulario = AventureroForm(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Aventurero(nombre = info['nombre'], apellido = info['apellido'], edad = info['edad'])
            info.save()
            return render(request, 'AppCoder/index.html')
    else:
        miFormulario = AventureroForm()
    return render(request, "AppCoder/aventureroForm.html",{'miFormulario':miFormulario})

def instructorForm(request):
    if request.method == 'POST':
        miFormulario = InstructorForm(request.POST) #<- traigo del template los datos de los input
        print(miFormulario)
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            info = Instructor(nombre = info['nombre'], apellido = info['apellido'], edad = info['edad'], email= info['email'])
            info.save()
            return render(request, 'AppCoder/index.html')
    else:
        miFormulario = InstructorForm()
    return render(request, "AppCoder/instructorForm.html",{'miFormulario':miFormulario})
