# Generated by Django 5.0.2 on 2024-06-11 15:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nombre')),
                ('FCreacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'categosrias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='facha de publicacion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='BlogImg', verbose_name='Imagen')),
                ('Fcreacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('fedicion', models.DateTimeField(auto_now=True, verbose_name='fecha de edicion')),
                ('categorias', models.ManyToManyField(to='core.categoria', verbose_name='Categorias')),
                ('id_persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.usuario')),
            ],
            options={
                'verbose_name': 'Post',
            },
        ),
    ]
