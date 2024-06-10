from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor_artigo')
    conteudo = models.TextField()
    data_publicada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios_artigos')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor_comentarios')
    conteudo = models.TextField()
    data_criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.username}: {self.conteudo[:20]}'

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings_artigos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autor_rating')
    score = models.IntegerField()

    def __str__(self):
        return f'{self.score} para {self.artigo.titulo} (de {self.user.username})'
# Create your models here.
