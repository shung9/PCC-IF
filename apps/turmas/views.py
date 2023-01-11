from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.views import nameUser
from .models import Turma, Post
from .forms import CriarTurma
import random, string



@login_required()
def turmas(request):
    cc = nameUser(request)

    atividade = Post.objects.filter(tipo='atividade')
    print(atividade)

    context = {'atividades': atividade, 'user': cc}
    return render(request, 'turmas/turmas.html', context)

@login_required()
def participar(request):
    cc = nameUser(request)

    if request.method == 'POST':
        busca = request.POST.get('busca')
        turma = Turma.objects.get(codigo=busca)

        turma.participantes.add(request.user)
        return redirect('home')

    else:
        return render(request, 'turmas/participar.html', cc)    

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
            cdg = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for x in range(5))
            print(cdg)

        else:
            obj.codigo = cdg
            obj.adm = request.user
            obj.save()
            
        return redirect('home')
    

    context = {'form': CriarTurma, 'nameUser': cc}
    return render(request, 'turmas/criar.html', context)

