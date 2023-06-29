from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from home.views import nameUser
from .models import Turma, Post, Comentarios
from .forms import CriarTurma, criarPost
import random
from django.urls import reverse
from django.contrib import messages
import os
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@login_required()
def turmas(request, codigo):
    cc = nameUser(request)

    turma = Turma.objects.get(codigo=codigo)
    posts = Post.objects.filter(turmaPertecente=turma)
    participantes = turma.participantes.all()

    context = {
        'nameUser': cc,
        'avisos': posts.filter(tipo='aviso'),
        'atividades': posts.filter(tipo='atividade'),
        'trabalhos': posts.filter(tipo='trabalho'),
        'provas': posts.filter(tipo='prova'),
        'turma': turma,
        'participantes': participantes,
    }

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

            email_html = render_to_string('emails/novaPostagem.html', {'nome_usuario': request.user,'turma': turma.nome , 'titulo_postagem': obj.nome, 'conteudo_postagem': obj.descricao, 'url_postagem': 'http://127.0.0.1:1212/turmas/'+codigo})
            email_text = strip_tags(email_html)

            if tipo in ['prova', 'atividade']:
                Email = EmailMultiAlternatives(f'Uma Nova {tipo.capitalize()} foi postada', email_text, settings.EMAIL_HOST_USER, remetentes)
            else:
                Email = EmailMultiAlternatives(f'Um Novo {tipo.capitalize()} foi postado', email_text, settings.EMAIL_HOST_USER, remetentes)


            Email.attach_alternative(email_html, 'text/html')
            Email.send()
            return redirect('turmas:turmas', codigo=codigo)

        else:
            formPost = criarPost()

    else:
        formPost = criarPost()

    context = {'formPost': formPost, 'nameUser': cc,
               'turma': turma, 'tipo': tipo}
    return render(request, 'turmas/criarPost.html', context)


@login_required
def editarPost(request, post_id):
    cc = nameUser(request)

    post = Post.objects.get(id=post_id)
    turma = post.turmaPertecente
    valores = criarPost(instance=post).initial

    if request.method == 'POST':
        formPost = criarPost(request.POST, instance=post)

        if formPost.is_valid():
            obj = formPost.save(commit=False)
            obj.anexo = request.FILES.get('anexo', None)
            obj.save()
            return redirect('turmas:turmas', codigo=post.turmaPertecente.codigo)
    else:
        formPost = criarPost(instance=post)

    context = {'formPost': valores, 'nameUser': cc, 'turma': turma}
    return render(request, 'turmas/editarPost.html', context)




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


def excluirPost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def excluirComentario(request, comentario_id):
    comentario = Comentarios.objects.get(id=comentario_id)
    comentario.delete()
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


def listar_participantes(request, codigo):
    turma = Turma.objects.get(codigo=codigo)
    participantes = turmas.participantes.all()

    context = {
        'turma': turma,
        'participantes': participantes,
    }

    return render(request, 'turmas/turmas.html', context)