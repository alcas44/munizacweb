# Generated by Django 3.2.7 on 2021-10-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SolicitudApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitar',
            name='token',
            field=models.CharField(default='', max_length=800),
            preserve_default=False,
        ),
    ]
