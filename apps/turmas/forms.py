from django import forms
from .models import Turma, Post

class CriarTurma(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'descricao', 'cor']

class criarPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nome', 'descricao', 'dataEntrega', 'anexo']


