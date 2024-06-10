import json
from bandas.models import Banda, Album, Musica

# Apagar tudo
Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

# Import bandas
with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)
    for banda in bandas:
        Banda.objects.create(
            nome=banda['nome'],
            nacionalidade=banda['nacionalidade'],
            ano_criado=banda['ano_criado'],
            foto=banda['foto']
        )

# Import Albuns
with open('bandas/json/albums.json') as f:
    albums = json.load(f)
    for album in albums:
        Album.objects.create(
            nome=album['nome'],
            ano_criado=album['ano_criado'],
            capa=album['capa'],
            banda=Banda.objects.get(nome=album['banda'])
        )

# Importar Musica
with open('bandas/json/musicas.json') as f:
    musicas = json.load(f)
    for musica in musicas:
        Musica.objects.create(
            nome=musica['nome'],
            link=musica['link'],
            ano_criado=musica['ano_criado'],
            duracao=musica['duracao'],
            album=Album.objects.get(nome=musica['album'])
        )