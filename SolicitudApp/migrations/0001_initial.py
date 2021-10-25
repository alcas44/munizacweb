# Generated by Django 3.2.7 on 2021-10-25 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dpi', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('depa', models.CharField(max_length=100)),
                ('muni', models.CharField(max_length=100)),
                ('medio', models.CharField(max_length=100)),
                ('contenido', models.CharField(max_length=500)),
            ],
        ),
    ]