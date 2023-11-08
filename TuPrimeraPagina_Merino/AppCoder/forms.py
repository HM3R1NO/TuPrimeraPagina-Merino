from django import forms

class AficionadoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField (max_length=50)
    edad=forms.IntegerField()

class AventureroForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField (max_length=50)
    edad=forms.IntegerField()

class InstructorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField (max_length=50)
    edad=forms.IntegerField()
    email=forms.EmailField()