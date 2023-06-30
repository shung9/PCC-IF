from django.urls import path
from . import views

app_name = 'turmas'

urlpatterns = [
    path('', views.turmas, name='turmas'),
    path('participar', views.participar, name="participar"),
    path('criar', views.criar, name="criar"),
    path('<str:codigo>/editarTurma', views.editarTurma, name="editarTurma"),
<<<<<<< HEAD
    
    path('<str:codigo>/remover_participantes/', views.remover_participantes, name="remover_participantes"),



=======
>>>>>>> f100748969a7d827a7af745ea8431d122310e3e5
    path('excluirComentario/<int:comentario_id>', views.excluirComentario, name="excluirComentario"),
    path('excluirPost/<int:post_id>', views.excluirPost, name="excluirPost"),
    path('editarPost/<int:post_id>', views.editarPost, name="editarPost"),
    path('<str:codigo>', views.turmas, name='turmas'),
    path('<str:codigo>/<str:tipo>/novopost', views.novoPost, name="criarPost"),
    path('<str:codigo>/<int:id>', views.listarPost, name='post'),
    path('post/<int:post_id>/excluir-anexo/', views.excluirAnexo, name='excluirAnexo'),
]
