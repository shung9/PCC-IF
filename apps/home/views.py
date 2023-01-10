from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from turmas.models import Turma
from collections import Counter

def nameUser(request): 
    user = str(request.user)
    context = {'name': user[:2].upper()}
    return context


def home(request):
    user = nameUser(request)

    if request.user.is_authenticated:
        adm = Turma.objects.filter(adm=request.user)
        participantes = Turma.objects.filter(participantes=request.user)
        

    else:
        return render(request, 'home/index.html') 
        

    context = {'turmasadm': adm, 'turmaspart': participantes, 'user': user}
    return render(request, 'home/index.html', context)

