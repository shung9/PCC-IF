from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.views import nameUser
from .models import Turma
from .forms import CriarTurma
import random, string



@login_required()
def turmas(request):
    cc = nameUser(request)
    return render(request, 'turmas/turmas.html', cc)

@login_required()
def participar(request):
    cc = nameUser(request)
    return render(request, 'turmas/participar.html', cc)


@login_required()
def criar(request):
    cc = nameUser(request)
    
    if request.method == 'POST':
        form = CriarTurma(request.POST)
        
    else:        
        form = CriarTurma()

    if form.is_valid():
        obj = form.save(commit=False)

        cdg = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for x in range(5))

        while Turma.objects.filter(codigo = cdg).exists(): 
            print('existe')
            cdg = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for x in range(5))
            print(cdg)

        else:
            obj.codigo = cdg
            obj.save()
            print('cabou')
            
        return redirect('home')
    

    context = {'form': CriarTurma, 'nameUser': cc}
    return render(request, 'turmas/criar.html', context)

