from django.db import models

class Usuario(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True) 
    
    def __str__(self) -> str:
        return self.login