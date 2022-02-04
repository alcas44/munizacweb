# Generated by Django 3.2.9 on 2022-02-04 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EspacioApp', '0002_alter_infousuario_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('apellido', models.CharField(max_length=300)),
                ('dpi', models.CharField(max_length=13)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.CharField(max_length=8)),
                ('correo', models.EmailField(max_length=200)),
                ('nacimiento', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfilusuario',
                'verbose_name_plural': 'perfilusuarios',
            },
        ),
    ]