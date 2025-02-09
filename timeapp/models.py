from django.db import models

# Create your models here.
class Workspace(models.Model):
    nombre = models.CharField(max_length=255)

class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    encargado = models.ForeignKey('Usuario', on_delete=models.CASCADE)  # Relación con Usuario, se crea entre comillas porque el modelo de usuario es creado despues de este
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE) #el on_delete es para que si se elimina el workspace se eliminen las tareas asociadas
    fecha_finalizacion = models.DateField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apodo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.apodo