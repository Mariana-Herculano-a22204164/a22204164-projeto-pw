from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('<int:pk>/', views.detalhes_artigo, name='detalhes_artigo'),
    path('create/', views.artigo_create_view, name='artigo_create'),
    path('<int:pk>/edit/', views.artigo_edit_view, name='artigo_edit'),
    path('<int:pk>/delete/', views.artigo_delete_view, name='artigo_delete'),
    path('comment/<int:pk>/edit/', views.comment_edit_view, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete_view, name='comment_delete'),
    path('rating/<int:pk>/edit/', views.rating_edit_view, name='rating_edit'),
    path('rating/<int:pk>/delete/', views.rating_delete_view, name='rating_delete'),
]
