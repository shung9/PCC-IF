from django.urls import path
from . import views

urlpatterns = [
    path('', views.turmas, name='turmas'),
    path('participar', views.participar, name="participar"),
]