# Generated by Django 3.2.16 on 2023-03-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlawyer', '0019_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='feedback',
            name='time',
            field=models.TimeField(default=''),
        ),
    ]
