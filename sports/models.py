# Create your models here.
from django.db import models

class EventoDeportivo(models.Model):
    equipo_local = models.CharField(max_length=100)
    equipo_visitante = models.CharField(max_length=100)
    hora = models.DateTimeField()
    cuota = models.FloatField()

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"

class Apuesta(models.Model):
    usuario = models.CharField(max_length=100)
    evento = models.ForeignKey(EventoDeportivo, on_delete=models.CASCADE)
    monto = models.FloatField()
    equipo_apostado = models.CharField(max_length=100)
    resultado = models.BooleanField(default=None, null=True)  # None = pendiente

    def __str__(self):
        return f"Apuesta de {self.usuario} en {self.evento}"
