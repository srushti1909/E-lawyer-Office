# Generated by Django 3.2.16 on 2023-03-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlawyer', '0014_auto_20230317_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.TextField(default=''),
        ),
    ]
