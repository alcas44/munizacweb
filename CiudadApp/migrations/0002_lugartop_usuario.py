# Generated by Django 3.2.7 on 2021-10-18 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CiudadApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugartop',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
