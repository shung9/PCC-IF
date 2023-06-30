from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
<<<<<<< HEAD
        
=======
    
>>>>>>> f100748969a7d827a7af745ea8431d122310e3e5
    def __str__(self):
        return self.first_name