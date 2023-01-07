from django.db import models

class Avisos(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField()
    codigo = models.CharField(max_length=5, null=True, blank=True)

class Turma(models.Model):
    nome = models.CharField(max_length = 50, null = False, blank = False)
    descricao = models.TextField(max_length = 150, null = True, blank = True)
    cor = models.CharField(max_length = 7, null = True, blank = True)
    codigo = models.CharField(max_length = 5, null = False, blank = False)

    def __str__(self):
        return self.nome   