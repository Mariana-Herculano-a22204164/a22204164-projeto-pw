# Generated by Django 4.0.6 on 2024-03-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_album_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='nome',
            field=models.CharField(default='Pensa bem', max_length=100),
            preserve_default=False,
        ),
    ]