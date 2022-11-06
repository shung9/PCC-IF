from django.db import models

class Avisos(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    codigo = models.CharField(max_length=5, null=True, blank=True)