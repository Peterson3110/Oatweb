from django.db import models

# Create your models here.

class Estoque(models.Model):

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    Produtos = models.CharField(max_length=100)
    quantidade = models.BigIntegerField("Quantidade de Produtos",max_length=20)
    fornecedor = models.CharField(max_length=100)

    def str(self):
        return self.nome
