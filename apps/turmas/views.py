from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.views import nameUser
from .models import Turma, Post
from .forms import CriarTurma, criarPost
import random, string




@login_required()
def turmas(request, codigo):
    cc = nameUser(request)

    turma = Turma.objects.get(codigo=codigo)
    posts = Post.objects.filter(turmaPertecente=turma)

    context = {
        'nameUser': cc,
        'avisos': posts.filter(tipo='aviso'), 
        'atividades': posts.filter(tipo='atividade'),
        'trabalhos': posts.filter(tipo='trabalho'),
        'provas': posts.filter(tipo='prova'),
        'turma': turma
    }

    return render(request, 'turmas/turmas.html', context)

    
    


@login_required()
def novoPost(request, codigo, tipo):
    cc = nameUser(request)

    formPost = criarPost()
    turma = Turma.objects.get(codigo=codigo)
    

    if request.method == 'POST':
        formPost = criarPost(request.POST)        
        
        if formPost.is_valid():
            obj = formPost.save(commit=False)
            obj.turmaPertecente = turma
            obj.tipo = tipo
            obj.save()
            return redirect('turmas:turmas', codigo=codigo)
            
        else:
            formPost = criarPost()

    else:
        formPost = criarPost()


    context = {'formPost': formPost, 'nameUser': cc, 'turma': turma}
    return render(request, 'turmas/criarPost.html', context)


@login_required()
def participar(request):
    cc = nameUser(request)

    if request.method == 'POST':
        busca = request.POST.get('busca')
        turma = Turma.objects.get(codigo=busca)

        turma.participantes.add(request.user)
        return redirect('home')

    else:
        return render(request, 'turmas/participar.html', {'nameUser': cc})    

    return render(request, 'turmas/participar.html', {'nameUser': cc})


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

