from django.db import models

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    bandas = models.ManyToManyField(Banda)
    foto = models.ImageField(upload_to="Festivais/", default=None, null=True, blank=True)

    def __str__(self):
        return self.nome

# Create your models here.
