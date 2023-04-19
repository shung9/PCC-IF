from django.db import models
from django.contrib.auth.models import User

class Aluno(User):
    def __str__(self):
        return self.nome