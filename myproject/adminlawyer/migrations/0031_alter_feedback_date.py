# Generated by Django 3.2.16 on 2023-03-28 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlawyer', '0030_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
