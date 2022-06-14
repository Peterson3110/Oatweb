from django.db import models

# Create your models here.

class Catalogo(models.Model):

    nome = models.CharField('Nome do Produto',max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    valor = models.FloatField(max_length=100)




    def str (self):
        return self.nome
