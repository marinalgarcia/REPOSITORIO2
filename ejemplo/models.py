from django.db import models

# Create your models here.
class Familiar(models.Model):
      nombre = models.CharField(max_length=100)
      direccion = models.CharField(max_length=200)
      numero_pasaporte = models.IntegerField()

class Persona (models.Model):
      nombre = models.CharField(max_length=100)
      apellido = models.CharField(max_length=100)
      numero_documento = models.IntegerField()

class Vuelo (models.Model):
      aeropuerto_salida = models.CharField(max_length=100)
      aeropuerto_destino = models.CharField(max_length=100)
      numero_vuelo = models.IntegerField()

def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"