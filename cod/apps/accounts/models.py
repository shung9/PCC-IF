from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    
    def __str__(self):
        return self.first_name