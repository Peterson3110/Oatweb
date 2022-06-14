from django.db import models

# Create your models here.

class Usuario(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.BigIntegerField(max_length=14)
    cpf = models.IntegerField(max_length=11)
    nascimento = models.DateField(max_length=8)

    def str (self):
        return self.nome
