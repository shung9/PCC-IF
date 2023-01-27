from django import forms
from .models import Turma, Post
from tinymce.widgets import TinyMCE

class CriarTurma(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'descricao', 'cor']

class criarPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nome', 'descricao', 'dataEntrega', 'anexo']


