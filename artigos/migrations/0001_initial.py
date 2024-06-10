# Generated by Django 4.0.6 on 2024-04-29 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo', models.TextField()),
                ('data_publicada', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_artigo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_artigos', to='artigos.artigo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('data_criada', models.DateTimeField(auto_now_add=True)),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_artigos', to='artigos.artigo')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_comentarios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
