from django.contrib import admin

from .models import Banda,Album,Musica

class BandaAdmin(admin.ModelAdmin):
    search_fields = ["nome"]

class AlbunAdmin(admin.ModelAdmin):
    search_fields = ["nome", "banda__nome"]

class MusicaAdmin(admin.ModelAdmin):
    search_fields = ["nome", "link"]

admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbunAdmin)
admin.site.register(Musica, MusicaAdmin)

# Register your models here.
