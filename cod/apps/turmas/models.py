from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


class Turma(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=50, null=True, blank=True)
    cor = models.CharField(max_length=7, null=True, blank=True)
    codigo = models.CharField(max_length=5, null=False, blank=False)
    adm = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    participantes = models.ManyToManyField(User, related_name='participantes', null=True, blank=True)

    def __str__(self):
        return self.nome


class Post(models.Model):
    tipo = models.CharField(max_length=10, null=False, blank=False)
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField(max_length=250, null=True, blank=True)
    valor = models.CharField(max_length=10, null=True, blank=True)
    dataEntrega = models.DateField(null=True, blank=True)
    anexo = models.FileField(upload_to='uploads/', null=True, blank=True, default=None)
    turmaPertecente = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True)
    criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Comentarios(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=240, null=True, blank=True)
    dono = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

