# Generated by Django 3.2.7 on 2021-10-21 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InicioApp', '0010_oficina'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='oficina',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='InicioApp.oficina'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requisito',
            name='oficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InicioApp.oficina'),
        ),
    ]
