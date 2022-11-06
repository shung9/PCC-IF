from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def nameUser(request): 
    user = str(request.user)
    context = {'name': user[:2].upper()}
    return context


def home(request):
    user = nameUser(request)   
    return render(request, 'home/index.html', user)

