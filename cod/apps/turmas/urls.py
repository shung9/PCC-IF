from django.urls import path
from . import views

app_name = 'turmas'

urlpatterns = [
    path('', views.turmas, name='turmas'),
    path('participar', views.participar, name="participar"),
    path('criar', views.criar, name="criar"),
    path('excluirComentario/<int:comentario_id>', views.excluirComentario, name="excluirComentario"),
    path('excluirPost/<int:post_id>', views.excluirPost, name="excluirPost"),
    path('<str:codigo>', views.turmas, name='turmas'),
    path('<str:codigo>/<str:tipo>/novopost', views.novoPost, name="criarPost"),
    path('<str:codigo>/<int:id>', views.listarPost, name='post'),
    path('post/<int:post_id>/excluir-anexo/', views.excluirAnexo, name='excluirAnexo'),
]
