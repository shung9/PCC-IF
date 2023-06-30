from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth
from django.core.validators import validate_email


def login(request):
    # um simple
    # if request.method == 'POST'; 
    if request.method == 'POST':
        #return render(request, 'accounts/login.html') #nao vejo a utilidade

    username = request.POST.get('username')
    password = request.POST.get('password')

    # faz a verificação aqui, se o username existe, de os czmpos username e password nao sao vazios
    if username and password: #se nao sao empty(vazio, null etc..)
        if User.objects.filter(username=username).exists(): # se tem um usuário com username 
            # verificar a autenticidade 
            user = authenticate(username=username, password=password)

    if user:
           login(request, user)
           return redirect('home')
        
    
    else:
        messages.error(request, 'Usuário ou senha inválidos')
        return redirect('login')


def registrar(request):
    #se queres redireccionar todas os usuários conectados para página
    # bloqueiar o acesso a página login e registrar

    # if request.user.is_authenticated:
        #return redirect('home')
    if request.method == 'POST':
        #return render(request, 'accounts/registrar.html') # nao vejp a utilidade 

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('senha')

    # VALIDAÇÕES

    try:
        validate_email(email)
    except:
        messages.error(request, 'email inválido')
        return render(request, 'accounts/registrar.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, 'já existe uma conta com esse nome')
        return render(request, 'accounts/registrar.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'já existe uma conta com esse email')
        return render(request, 'accounts/registrar.html')
    #olha o login 

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    messages.success(request, 'cadastrado realizado! faça login')
    
    return redirect('accounts:login')
    
    

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

    
