# Generated by Django 3.2.16 on 2023-03-16 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminlawyer', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
