from django.db import models


# Create your models here.

class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self):
        return f'{self.nombre_curso} - {self.camada}'

class Inscripcion(models.Model):
    nombre_alumno = models.CharField(max_length=50)
    apellido_alumno = models.CharField(max_length=50)
    email_alumno = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.nombre_alumno} - {self.apellido_alumno} - {self.email_alumno}'

class Entregables(models.Model):
    nombre_alumno = models.CharField(max_length=50)
    nombre_trabajo_entegable = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre_alumno} - {self.nombre_trabajo_entegable}'