from django import forms
from .models import Turma

class CriarTurma(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'descricao', 'cor']


