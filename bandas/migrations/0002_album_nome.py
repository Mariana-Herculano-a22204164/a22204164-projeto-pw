# Generated by Django 4.0.6 on 2024-03-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='nome',
            field=models.CharField(default='NA', max_length=100),
            preserve_default=False,
        ),
    ]
