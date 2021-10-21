# Generated by Django 3.2.7 on 2021-10-19 16:48

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
            name='CategoriaNoticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'categorianoticia',
                'verbose_name_plural': 'categoriasnoticias',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='noticias')),
                ('ubicacion', models.CharField(blank=True, max_length=100, null=True)),
                ('oficina', models.CharField(blank=True, max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NoticiasApp.categorianoticia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'noticia',
                'verbose_name_plural': 'noticias',
            },
        ),
        migrations.CreateModel(
            name='FotosNoticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='noticias/fotosnoticia')),
                ('oficina', models.CharField(blank=True, max_length=150, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NoticiasApp.noticia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'fotonoticia',
                'verbose_name_plural': 'fotosnoticias',
            },
        ),
    ]
