from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

def curso(self):
    curso = Curso(nombre="Django", comision=96)
    curso.save()
    texto=f"Curso creado: {curso.nombre},{curso.comision}"
    return HttpResponse(texto)
    