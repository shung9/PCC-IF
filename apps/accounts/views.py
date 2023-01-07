from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth
from django.core.validators import validate_email


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos')
        return render(request, 'accounts/login.html')
    
    else:
        auth.login(request, user)
        return redirect('home')



def registrar(request):
    if request.method != 'POST':
        return render(request, 'accounts/registrar.html')

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

    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    messages.success(request, 'cadastrado realizado! faça login')
    
    return redirect('accounts:login')
    
    

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

    
