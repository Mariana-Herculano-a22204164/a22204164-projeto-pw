from django.contrib import admin
from .models import Curso, AreaCientifica, Disciplina, Docente, LinguagemProgramacao, Projeto

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apresentacao', 'objetivos', 'competencias')
    search_fields = ('nome', 'competencias')
    list_filter = ('nome',)
    ordering = ('nome',)

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo')
    search_fields = ('nome',)
    list_filter = ('nome',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano', 'semestre', 'ects', 'curricular_unit_readable_code', 'area_cientifica')
    search_fields = ('nome', 'curricular_unit_readable_code')
    list_filter = ('ano', 'semestre', 'area_cientifica')

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    filter_horizontal = ('disciplinas',)

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'disciplina', 'link_video', 'link_github')
    search_fields = ('descricao', 'disciplina__nome')
    list_filter = ('disciplina',)

admin.site.register(Curso, CursoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(Projeto, ProjetoAdmin)


# Register your models here.
