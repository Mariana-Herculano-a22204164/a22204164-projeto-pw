from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Banda, Album, Musica
from .forms import MusicaForm, AlbumForm, BandaForm

#! Bandas #!

def bandas_list_view(request):
    bandas = Banda.objects.all()
    is_editor = request.user.groups.filter(name="Editores de Bandas").exists()
    context = {'bandas': bandas,'is_editor': is_editor}
    return render(request, 'bandas/bandas_list.html', context)

def banda_detail_view(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    albums = banda.album_set.all()
    is_editor = request.user.groups.filter(name="Editores de Bandas").exists()
    context = {'banda': banda, 'albums': albums,'is_editor': is_editor}
    return render(request, 'bandas/banda_detail.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def banda_create_view(request):
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas_list')
    else:
        form = BandaForm()
    return render(request, 'bandas/banda_create.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def banda_edit_view(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'POST':
        form = BandaForm(request.POST, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:banda_detail', banda_id=banda_id)
    else:
        form = BandaForm(instance=banda)
    return render(request, 'bandas/banda_edit.html', {'form': form, 'banda': banda})

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def banda_delete_view(request, banda_id):
    banda = get_object_or_404(Banda, id=banda_id)
    if request.method == 'GET':
        banda.delete()
        return redirect('bandas:bandas_list')
    return redirect('bandas:banda_detail', banda_id=banda_id)

#! Albuns #!
def album_detail_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    musicas = album.musica_set.all()
    is_editor = request.user.groups.filter(name="Editores de Bandas").exists()
    context = {'album': album, 'musicas': musicas,'is_editor': is_editor}
    return render(request, 'bandas/album_detail.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def album_create_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandas_list')
    else:
        form = AlbumForm()
    return render(request, 'bandas/album_create.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def album_edit_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album_detail', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'bandas/album_edit.html', {'form': form, 'album': album})

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def album_delete_view(request, musica_id):
    album = get_object_or_404(Album, id=musica_id)
    if request.method == 'POST':
        album.delete()
        return redirect('bandas:bandas_list')
    return redirect('bandas:album_detail', musica_id=album.id)

#! Musicas #!

def musica_detail_view(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)
    album = musica.album
    banda = album.banda
    is_editor = request.user.groups.filter(name="Editores de Bandas").exists()
    context = {'musica': musica, 'album': album, 'banda': banda, 'is_editor': is_editor}
    return render(request, 'bandas/musica_detail.html', context)

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def musica_create_view(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, request.FILES)
        if form.is_valid():
            new_musica = form.save(commit=False)
            new_musica.album = album
            new_musica.save()
            return redirect('bandas:album_detail', album_id=album.id)
    else:
        form = MusicaForm()
    return render(request, 'bandas/musica_create.html', {'form': form, 'album': album})

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def musica_edit_view(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)
    if request.method == 'POST':
        form = MusicaForm(request.POST, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musica_detail', musica_id=musica.id)
    else:
        form = MusicaForm(instance=musica)
    return render(request, 'bandas/musica_edit.html', {'form': form, 'musica': musica})

@login_required
@user_passes_test(lambda u: u.groups.filter(name="Editores de Bandas").exists())
def musica_delete_view(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)
    if request.method == 'POST':
        musica.delete()
        return redirect('bandas:bandas_list')
    return redirect('bandas:musica_detail', musica_id=musica.id)
