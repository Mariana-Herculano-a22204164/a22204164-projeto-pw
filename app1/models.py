from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()



    def __str__(self):
        return f'{self.nome} - {self.idade} anos'

class Alunos(models.Model):
    primeironome = models.CharField(max_length = 100)


# Create your models here.
