from django import forms
from .models import Curso, Disciplina, Projeto

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'apresentacao', 'objetivos', 'competencias', 'codigo_curso']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'apresentacao': forms.TextInput(attrs={'class': 'form-control'}),
            'objetivos': forms.TextInput(attrs={'class': 'form-control'}),
            'competencias': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_curso': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Curso',
            'apresentacao': 'Apresentação',
            'objetivos': 'Objetivos',
            'competencias': 'Competências',
            'codigo_curso': 'Código de Curso',
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'ano', 'semestre', 'ects', 'curricular_unit_readable_code', 'area_cientifica']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'semestre': forms.TextInput(attrs={'class': 'form-control'}),
            'ects': forms.NumberInput(attrs={'class': 'form-control'}),
            'curricular_unit_readable_code': forms.TextInput(attrs={'class': 'form-control'}),
            'area_cientifica': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome da Disciplina',
            'ano': 'Ano',
            'semestre': 'Semestre',
            'ects': 'Créditos ECTS',
            'curricular_unit_readable_code': 'Código Curricular',
            'area_cientifica': 'Área Cientifica',
        }

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'conceitos_aplicados', 'tecnologias_usadas', 'imagem_url', 'link_video', 'link_github', 'disciplina', 'linguagens']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'conceitos_aplicados': forms.TextInput(attrs={'class': 'form-control'}),
            'tecnologias_usadas': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem_url': forms.URLInput(attrs={'class': 'form-control'}),
            'link_video':  forms.URLInput(attrs={'class': 'form-control'}),
            'link_github': forms.URLInput(attrs={'class': 'form-control'}),
            'disciplina': forms.Select(attrs={'class': 'form-control'}),
            'linguagens': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Projeto',
            'descricao': 'Descrição',
            'conceitos_aplicados': 'Conceitos Aplicados',
            'tecnologias_usadas': 'Tecnologias Usadasd',
            'imagem_url': 'Imagem',
            'link_video': 'Link Video',
            'link_github': 'Link Github',
            'disciplina': 'Disciplina',
            'linguagens': 'Linguagem',
        }
