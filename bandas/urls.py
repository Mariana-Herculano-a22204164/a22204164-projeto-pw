from django.urls import path
from . import views

app_name = 'bandas'
urlpatterns = [
    path('', views.bandas_list_view, name='bandas_list'),
    # Bandas
    path('banda/<int:banda_id>/', views.banda_detail_view, name='banda_detail'),
    path('banda/create/', views.banda_create_view, name='banda_create'),
    path('banda/edit/<int:banda_id>/', views.banda_edit_view, name='banda_edit'),
    path('banda/delete/<int:banda_id>/', views.banda_delete_view, name='banda_delete'),

    # Albums
    path('album/<int:album_id>/', views.album_detail_view, name='album_detail'),
    path('album/create/', views.album_create_view, name='album_create'),
    path('album/edit/<int:album_id>/', views.album_edit_view, name='album_edit'),
    path('album/delete/<int:album_id>/', views.album_delete_view, name='album_delete'),
    
    # Musicas
    path('musica/<int:musica_id>/', views.musica_detail_view, name='musica_detail'),
    path('musica/create/<int:album_id>/', views.musica_create_view, name='musica_create'),
    path('musica/edit/<int:musica_id>/', views.musica_edit_view, name='musica_edit'),
    path('musica/delete/<int:musica_id>/', views.musica_delete_view, name='musica_delete'),
]