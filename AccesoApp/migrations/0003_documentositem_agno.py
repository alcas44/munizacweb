# Generated by Django 3.2.7 on 2021-10-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccesoApp', '0002_documentositem_folderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentositem',
            name='agno',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
    ]
