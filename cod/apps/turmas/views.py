from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from email.utils import make_msgid
from home.views import nameUser
from .models import Turma, Post, Comentarios
from .forms import CriarTurma, criarPost
import random
import string
import threading
from django.urls import reverse
from .tasks import enviar_email
from django.contrib import messages
import os
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.conf import settings
from django.views.decorators.http import require_POST

@login_required()
def turmas(request, codigo):
    cc = nameUser(request)

    turma = Turma.objects.get(codigo=codigo)
    posts = Post.objects.filter(turmaPertecente=turma)
    participantes = turma.participantes.all()
    print(participantes)

    context = {
        'nameUser': cc,
        'avisos': posts.filter(tipo='aviso'),
        'atividades': posts.filter(tipo='atividade'),
        'trabalhos': posts.filter(tipo='trabalho'),
        'provas': posts.filter(tipo='prova'),
        'turma': turma,
        'participantes': participantes,
    }

    # enviar_email.delay(cc, cc)

    return render(request, 'turmas/turmas.html', context)


@login_required()
def participar(request):
    cc = nameUser(request)

    if request.method == 'POST':
        busca = request.POST.get('busca')

        turma = Turma.objects.filter(codigo=busca).first()

        if turma:
            turma.participantes.add(request.user)
            return redirect('home')

        else:
            messages.error(request, 'Código inválido')
            return render(request, 'turmas/participar.html', {'nameUser': cc})

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

        cdg = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
                      for x in range(5))

        while Turma.objects.filter(codigo=cdg).exists():
            cdg = ''.join(random.choice(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for x in range(5))
            print(cdg)

        else:
            obj.codigo = cdg
            obj.adm = request.user
            obj.save()

        return redirect('home')

    context = {'form': CriarTurma, 'nameUser': cc}
    return render(request, 'turmas/criar.html', context)


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
            obj.anexo = request.FILES.get('anexo', None)
            obj.save()

            participantes = turma.participantes.all()
            remetentes = [participante.email for participante in participantes]

            # if tipo in ['prova', 'atividade']:
            #    send_mail('Nova Postagem', f'Uma nova {tipo} foi criada na turma {turma}\n\n{obj.nome}', 'suport.class.school@gmail.com', remetentes)
            # else:
            #    send_mail('Nova Postagem', f'Um novo {tipo} foi criado na turma {turma}\n\n{obj.nome}', 'suport.class.school@gmail.com', remetentes)

           # if tipo in ['prova', 'atividade']:
            # send_mail(
            #   'Nova Postagem', f'Uma nova {tipo} foi criada na turma {turma}\n\n{obj.nome}', 'suport.class.school@gmail.com', remetentes)
            # else:
            # send_mail(
            #  'Nova Postagem', f'Um novo {tipo} foi criado na turma {turma}\n\n{obj.nome}', 'suport.class.school@gmail.com', remetentes)

            # return redirect('turmas:turmas', codigo=codigo)

        else:
            formPost = criarPost()

    else:
        formPost = criarPost()

    context = {'formPost': formPost, 'nameUser': cc,
               'turma': turma, 'tipo': tipo}
    return render(request, 'turmas/criarPost.html', context)


@login_required()
def listarPost(request, codigo, id):
    cc = nameUser(request)

    listaPost = Post.objects.get(id=id)
    url = reverse('turmas:post', args=[codigo, id])

    if request.method == 'POST':
        coment = request.POST.get('coment')

        if coment:
            novoComentario = Comentarios(
            post=listaPost, comentario=coment, dono=request.user)
            novoComentario.save()
            return redirect('turmas:post', codigo=codigo, id=id)

    context = {'nameUser': cc,
               'post': listaPost,
               'comentarios': Comentarios.objects.filter(post=listaPost),
               'url': url
               }

    return render(request, 'turmas/post.html', context)


def excluirComentario(request, comentario_id):
    comentario = Comentarios.objects.get(id=comentario_id)
    comentario.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def excluirPost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def excluirAnexo(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if not (request.user):
        raise PermissionDenied  
    if post.anexo:
        caminho_arquivo = os.path.join(settings.MEDIA_ROOT, str(post.anexo))
        
       
        if os.path.exists(caminho_arquivo):
            # Exclui o arquivo
            os.remove(caminho_arquivo)
            post.anexo = None
            post.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def calendario (request):
    return render(request, 'turmas:rew.html')

def listar_participantes(request, codigo):
    turma = Turma.objects.get(codigo=codigo)
    participantes = turmas.participantes.all()
    print(participantes)

    context = {
        'turma': turma,
        'participantes': participantes,
    }

    return render(request, 'turmas/turmas.html', context)