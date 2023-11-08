from django.db import models

class Aficionado(models.Model):
    nombre=models.CharField(max_length=50)
    Apellido=models.CharField (max_length=50)
    edad=models.IntegerField()

class Aventurero(models.Model):
    nombre=models.CharField(max_length=50)
    Apellido=models.CharField (max_length=50)
    edad=models.IntegerField()

class Instructor(models.Model):
    nombre=models.CharField(max_length=50)
    Apellido=models.CharField (max_length=50)
    email=models.EmailField()