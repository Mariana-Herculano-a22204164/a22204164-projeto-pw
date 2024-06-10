from django.urls import path
from . import views

app_name = 'curso'
urlpatterns = [
    path('', views.cursos_list_view, name='cursos_list'),
    path('curso/<int:curso_id>/', views.curso_detail_view, name='curso_detail'),
    path('curso/create', views.curso_create_view, name="curso_create"),
    path('curso/edit/<int:curso_id>', views.curso_edit_view, name="curso_edit"),
    path('curso/delete/<int:curso_id>', views.curso_delete_view, name="curso_delete"),

    path('disciplina/<int:disciplina_id>/', views.disciplina_detail_view, name='disciplina_detail'),
    path('disciplina/create', views.disciplina_create_view, name="disciplina_create"),
    path('disciplina/edit/<int:disciplina_id>', views.disciplina_edit_view, name="disciplina_edit"),
    path('disciplina/delete/<int:disciplina_id>', views.disciplina_delete_view, name="disciplina_delete"),

    path('projeto/<int:projeto_id>/', views.projeto_detail_view, name='projeto_detail'),
    path('projeto/create', views.projeto_create_view, name="projeto_create"),
    path('projeto/edit/<int:projeto_id>', views.projeto_edit_view, name="projeto_edit"),
    path('projeto/delete/<int:projeto_id>', views.projeto_delete_view, name="projeto_delete"),
]