from django import forms

class CursosFormulario(forms.Form):
    nombre_curso = forms.CharField()
    camada = forms.IntegerField()

class InscripcionFormulario(forms.Form):
    nombre_alumno = forms.CharField()
    apellido_alumno = forms.CharField()
    email_alumno = forms.EmailField()

class EntregablesFormulario(forms.Form):
    nombre_alumno = forms.CharField()
    nombre_trabajo_entegable = forms.CharField()
