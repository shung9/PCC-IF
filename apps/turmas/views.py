from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.views import nameUser



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
    return render(request, 'turmas/criar.html', cc)

