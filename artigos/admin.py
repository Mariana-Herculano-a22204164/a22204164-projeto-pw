from django.contrib import admin
from .models import Artigo, Comentario, Rating

class ComentatioInline(admin.TabularInline):
    model = Comentario
    extra = 1
    fields = ('autor', 'conteudo', 'data_criada')
    readonly_fields = ('data_criada',)

class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    fields = ('user', 'score')

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicada', 'id')
    list_filter = ('data_publicada', 'autor')
    search_fields = ('titulo', 'conteudo')
    inlines = [ComentatioInline, RatingInline]
    readonly_fields = ('data_publicada',)

admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario)
admin.site.register(Rating)

# Register your models here.
