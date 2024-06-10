from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    codigo_curso = models.CharField(max_length=20, null=True, blank=True)

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.IntegerField()
    codigo_cnaef = models.TextField()

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    curricular_unit_readable_code = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem_url = models.URLField()
    link_video = models.URLField()
    link_github = models.URLField()
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    linguagens = models.ManyToManyField(LinguagemProgramacao)

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    disciplinas = models.ManyToManyField(Disciplina, related_name="docentes")

# Create your models here.
