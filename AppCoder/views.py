from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Profesor
from .forms import CursoFormulario1, ProfesorFormulario1

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

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario1(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=request.POST['nombre'], camada=request.POST['camada'])
        curso.save()
        return render(request,"inicio.html")
    else:
        miFormulario = CursoFormulario1()

    return render(request, "cursoFormulario.html", {"miFormulario":miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario1(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], profesion=request.POST['profesion'])
        profesor.save()
        return render(request,"inicio.html")
    else:
        miFormulario = ProfesorFormulario1()

    return render(request, "profesorFormulario.html", {"miFormulario":miFormulario})

def busquedaCamada(request):
    return render(request, 'busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)
        return render(request, 'resultadosBusqueda.html', {"cursos":curso, "camada":camada})
    else:
        respuesta = "No enviaste datos."
    return HttpResponse(respuesta)
