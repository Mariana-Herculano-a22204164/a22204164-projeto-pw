# Generated by Django 4.0.6 on 2024-04-24 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('festivais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='festival',
            name='foto',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Festivais/'),
        ),
    ]
