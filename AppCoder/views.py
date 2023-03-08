from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def curso(self):
#    curso = Curso(nombre='Desarrollo Web', camada=12345)
#    curso.save()
#    documentoDeTexto = f'--->Curso: {curso.nombre} Camada: {curso.camada}'
#    return  HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')
