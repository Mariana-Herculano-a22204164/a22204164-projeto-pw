from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Artigo, Comentario, Rating
from .forms import CommentForm, RatingForm, ArtigoForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_editor(user):
    return user.groups.filter(name="Editores de Artigos").exists()


def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'artigos/lista_artigos.html', {'artigos': artigos})


def detalhes_artigo(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    comment_form = CommentForm()
    rating_form = RatingForm()

    if request.method == 'POST':
        if 'comentario' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                if request.user.is_authenticated:
                    comment.artigo = artigo
                    comment.autor = request.user
                    comment.save()
                    return redirect('artigos:detalhes_artigo', pk=artigo.pk)
                else:
                    login_url = f"{reverse('login')}?next={request.path}"
                    return redirect(login_url)
        elif 'rating' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                if request.user.is_authenticated:
                    rating.artigo = artigo
                    rating.user = request.user
                    rating.save()
                    return redirect('artigos:detalhes_artigo', pk=artigo.pk)
                else:
                    login_url = f"{reverse('login')}?next={request.path}"
                    return redirect(login_url)

    return render(request, 'artigos/detalhes_artigo.html', {
        'artigo': artigo,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'is_editor': is_editor(request.user)
    })


@login_required
@user_passes_test(is_editor)
def artigo_create_view(request):
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artigos:lista_artigos')
    else:
        form = ArtigoForm()
    return render(request, 'artigos/artigo_form.html', {'form': form})


@login_required
@user_passes_test(is_editor)
def artigo_edit_view(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_artigo', pk=pk)
    else:
        form = ArtigoForm(instance=artigo)
    return render(request, 'artigos/artigo_form.html', {'form': form, 'artigo': artigo})


@login_required
@user_passes_test(is_editor)
def artigo_delete_view(request, pk):
    artigo = get_object_or_404(Artigo, pk=pk)
    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos:lista_artigos')
    return render(request, 'artigos/artigo_confirm_delete.html', {'artigo': artigo})


@login_required
@user_passes_test(is_editor)
def comment_edit_view(request, pk):
    comment = get_object_or_404(Comentario, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            if request.user.is_authenticated:
                form.save()
                return redirect('artigos:detalhes_artigo', pk=comment.artigo.pk)
            else:
                return redirect('login')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'artigos/comment_form.html', {'form': form, 'comment': comment})


@login_required
@user_passes_test(is_editor)
def comment_delete_view(request, pk):
    comment = get_object_or_404(Comentario, pk=pk)
    artigo_id = comment.artigo.id
    if request.method == 'POST':
        comment.delete()
        return redirect('artigos:detalhes_artigo', pk=artigo_id)
    return render(request, 'artigos/comment_confirm_delete.html', {'comment': comment})


@login_required
@user_passes_test(is_editor)
def rating_edit_view(request, pk):
    rating = get_object_or_404(Rating, pk=pk)
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhes_artigo', pk=rating.artigo.pk)
    else:
        form = RatingForm(instance=rating)
    return render(request, 'artigos/rating_form.html', {'form': form, 'rating': rating})


@login_required
@user_passes_test(is_editor)
def rating_delete_view(request, pk):
    rating = get_object_or_404(Rating, pk=pk)
    artigo_id = rating.artigo.id
    if request.method == 'POST':
        rating.delete()
        return redirect('artigos:detalhes_artigo', pk=artigo_id)
    return render(request, 'artigos/rating_confirm_delete.html', {'rating': rating})
