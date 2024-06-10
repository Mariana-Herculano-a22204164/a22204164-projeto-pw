from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CursoForm, DisciplinaForm, ProjetoForm
from .models import Curso, Disciplina, Projeto

def is_editor(user):
    return user.groups.filter(name="Editores de Curso").exists()

#! Curso
def cursos_list_view(request):
    cursos = Curso.objects.all()
    context = { 'cursos': cursos, 'is_editor': is_editor(request.user)}
    return render(request, 'curso/cursos_list.html', context)

def curso_detail_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    disciplinas = Disciplina.objects.filter(curricular_unit_readable_code__startswith=curso.codigo_curso)
    context = {'curso': curso, 'disciplinas': disciplinas, 'is_editor': is_editor(request.user)}
    return render(request, 'curso/curso_detail.html', context)

@login_required
@user_passes_test(is_editor)
def curso_create_view(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:cursos_list')
    else:
        form = CursoForm()
    return render(request, 'curso/curso_form.html', {'form': form, 'id_editor': is_editor(request.user)})

@login_required
@user_passes_test(is_editor)
def curso_edit_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso:curso_detail')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso/curso_form.html', {'form': form, 'curso': curso, 'is_editor': is_editor(request.user)})

@login_required
@user_passes_test(is_editor)
def curso_delete_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso:cursos_list')
    return render(request, 'curso/curso_confirm_delete.html', {'curso': curso, 'is_editor': is_editor(request.user)})

#! Disciplina
def disciplina_detail_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    curso_code = disciplina.curricular_unit_readable_code.split('-')[0]
    curso = Curso.objects.filter(codigo_curso=curso_code).first()
    projeto = None
    try:
        projeto = Projeto.objects.get(disciplina=disciplina)
    except Projeto.DoesNotExist:
        pass
    context = {'disciplina': disciplina, 'projeto': projeto, 'curso': curso, 'is_editor': is_editor(request.user)}
    return render(request, 'curso/disciplina_detail.html', context)

@login_required
@user_passes_test(is_editor)
def disciplina_create_view(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:cursos_list')
    else:
        form = DisciplinaForm()
    return render(request, 'curso/disciplina_form.html', {'form': form, 'is_editor': is_editor(request.user)})

@login_required
@user_passes_test(is_editor)
def disciplina_edit_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina_detail')
    else:
        form = DisciplinaForm(instance=disciplina)
    return render(request, 'curso/disciplina_form.html', {'form': form, 'disciplina': disciplina, 'is_editor': is_editor(request.user)})

@login_required
@user_passes_test(is_editor)
def disciplina_delete_view(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('curso:cursos_list')
    return render(request, 'curso/disciplina_confirm_delete.html', {'disciplina': disciplina, 'is_editor': is_editor(request.user)})

#! Projeto
def projeto_detail_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    disciplina = projeto.disciplina
    curso_code = disciplina.curricular_unit_readable_code.split('-')[0]
    curso = Curso.objects.filter(codigo_curso=curso_code).first()
    context = {'projeto': projeto, 'disciplina': disciplina, 'curso': curso, 'is_editor': is_editor(request.user)}
    return render(request, 'curso/projeto_detail.html', context)

@login_required
@user_passes_test(is_editor)
def projeto_create_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso:cursos_list')
    else:
        form = ProjetoForm()
    return render(request, 'curso/projeto_form.html', {'form': form, 'is_editor': is_editor(request.user)})

@login_required
@user_passes_test(is_editor)
def projeto_edit_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto_detail')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'curso/projeto_form.html', {'form': form, 'projeto': projeto, 'is_editor': is_editor(request.user)})

@login_required
@user_passes_test(is_editor)
def projeto_delete_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('curso:cursos_list')
    return render(request, 'curso/projeto_confirm_delete.html', {'projeto': projeto, 'is_editor': is_editor(request.user)})



# Create your views here.
