from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def inicio(request):

    return render(request, 'index.html')

def buscar(request):

    if request.GET["camada"]:
        camada = request.GET["camada"]
        curso = Cursos.objects.filter(camada=camada)
        return render(request, "resultado.html", {"curso": curso, "camada": camada})
    else:
        return HttpResponse('No hay ningun Curso con esa camada')

def inscripcion(request):
    if request.method == 'POST':
        
        miFormulario = InscripcionFormulario(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            inscripcion = Inscripcion(nombre_alumno=data_formulario['nombre_alumno'], apellido_alumno=data_formulario['apellido_alumno'],email_alumno=data_formulario['email_alumno'])
            inscripcion.save()
            return render(request, 'index.html')
    else:
        miFormulario = InscripcionFormulario()

        return render(request, 'inscripcion.html',{'miFormulario': miFormulario})



    return render(request, 'inscripcion.html')
def cursos(request):

    if request.method == 'POST':
        miFormulario = CursosFormulario(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            curso = Cursos(nombre_curso=data_formulario['nombre_curso'], camada=data_formulario['camada'])
            curso.save()
            return render(request, 'index.html')
    else:
        miFormulario = CursosFormulario()

        return render(request, 'cursos.html',{'miFormulario': miFormulario})



def entregables(request):
    if request.method == 'POST':
        
        miFormulario = EntregablesFormulario(request.POST)
        
        if miFormulario.is_valid():

            data_formulario = miFormulario.cleaned_data

            entregables = Entregables(nombre_alumno=data_formulario['nombre_alumno'], nombre_trabajo_entegable=data_formulario['nombre_trabajo_entegable'])
            entregables.save()
            return render(request, 'index.html')
    else:
        miFormulario = EntregablesFormulario()

        return render(request, 'entregables.html',{'miFormulario': miFormulario})
