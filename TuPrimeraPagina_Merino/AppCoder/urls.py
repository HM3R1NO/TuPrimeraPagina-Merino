from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="home"),
    path("aficionadoForm/", aficionadoForm, name="aficionado"),
    path("aventureroForm/", aventureroForm, name="aventurero"),
    path("instructorForm/", instructorForm, name="instructor"),
]
