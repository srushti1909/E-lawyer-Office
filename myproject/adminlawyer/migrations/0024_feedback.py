# Generated by Django 3.2.16 on 2023-03-28 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminlawyer', '0023_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='01/01/2000')),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('rating', models.IntegerField()),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.cases')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
