from django.db import models

# Create your models here.
class Partida(models.Model):
    jogador = models.CharField(max_length=10)
    computador = models.CharField(max_length=10)
    resultado = models.CharField(max_length=10)
    criada_em = models.DateTimeField(auto_now_add=True)