# Generated by Django 3.2.16 on 2023-03-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlawyer', '0024_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(default='2000/01/01'),
        ),
    ]
