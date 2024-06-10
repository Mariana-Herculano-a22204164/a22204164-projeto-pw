from django import forms
from .models import Comentario, Rating, Artigo


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['conteudo']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'conteudo']
