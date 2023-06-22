from django.shortcuts import render, redirect
from turmas.models import Turma, Post
import json


def calendario(request, codigo):

   turma = Turma.objects.get(codigo=codigo)
   posts = Post.objects.filter(turmaPertecente=turma)

   out = []
   for post in posts:
      out.append({
         'id': post.id,
         'title': post.nome,
         'start': post.dataEntrega.strftime("%Y-%m-%d"),
         'description': post.descricao,
         'color': 'red',
         'extendedProps': {
               'description1': 'BioChemistry'
         }
      })

   context = {
      'posts_json': json.dumps(out)
   }

   return render(request, 'calendario/calendario.html', context)







