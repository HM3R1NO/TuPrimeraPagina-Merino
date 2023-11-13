from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre= models.CharField(max_length=30)
    camada= models.IntegerField()

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email=models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email=models.EmailField()
    edad= models.IntegerField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Edad: {self.edad}'
