from django import forms
from .models import Musica, Album, Banda

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['nome', 'link', 'ano_criado', 'duracao', 'album']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'ano_criado': forms.NumberInput(attrs={'class': 'form-control'}),
            'duracao': forms.TimeInput(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome da Música',
            'link': 'Link para Ouvir',
            'ano_criado': 'Ano de Criação',
            'duracao': 'Duração',
            'album': 'Álbum',
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nome', 'ano_criado', 'capa', 'banda']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_criado': forms.NumberInput(attrs={'class': 'form-control'}),
            'capa': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'banda': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Album',
            'ano_criado': 'Ano de Criação',
            'capa': 'Capa',
            'banda': 'Banda',
        }

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nome', 'nacionalidade', 'ano_criado', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_criado': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome da banda',
            'nacionalidade': 'Nacionalidade da banda',
            'ano_criado': 'Ano de Criação',
        }
