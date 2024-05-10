# importa o módulo 'models' que contém as classes para definir os models do db.
from django.db import models

# class Produto que herda de 'models.Model'. Produto é um modelo de db do Django
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    quantidade = models.CharField(max_length=20)

    # método que retorna uma representação de string do objeto
    def __str__(self):
        return self.nome