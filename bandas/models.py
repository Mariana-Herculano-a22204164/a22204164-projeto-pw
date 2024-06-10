from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    ano_criado = models.IntegerField(max_length=4)
    foto = models.ImageField(upload_to = 'uploads/', blank=True)

    def str(self):
        return f'{self.nome} / {self.nacionalidade} / {self.ano_criado}'

class Album(models.Model):
    nome = models.CharField(max_length=100)
    ano_criado = models.IntegerField(max_length=4)
    capa = models.ImageField(upload_to = 'uploads/', blank=True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

    def str(self):
        return f'{self.nome} - {self.banda} - {self.ano_criado}'

class Musica(models.Model):
    nome = models.CharField(max_length=100)
    link = models.URLField(max_length=100, blank=True)
    ano_criado = models.IntegerField(max_length=4, blank=True)
    duracao = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def str(self):
        return f'{self.nome} / {self.ano_criado} / {self.duracao}'