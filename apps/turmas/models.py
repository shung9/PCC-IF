from django.db import models
from django.contrib.auth.models import User


class Avisos(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    codigo = models.CharField(max_length=5, null=True, blank=True)

class Turma(models.Model):
    nome = models.CharField(max_length = 50, null = False, blank = False)
    descricao = models.TextField(max_length = 150, null = True, blank = True)
    cor = models.CharField(max_length = 7, null = True, blank = True)
    codigo = models.CharField(max_length = 5, null = False, blank = False)
    adm = models.ForeignKey(User, on_delete=models.SET_NULL, null = True) 
    participantes = models.ManyToManyField(User, related_name='participantes', null = True, blank = True)

    def __str__(self):
        return self.nome   

class Post(models.Model):
    tipo = models.CharField(max_length = 10, null = False, blank = False)
    nome = models.CharField(max_length = 50, null = False, blank = False)
    descricao = models.TextField(max_length = 250, null = True, blank = True)
    dataEntrega = models.DateField(null = True, blank = True)
    anexo = models.FileField(null = True, blank = True)
    turmaPertecente = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome
    