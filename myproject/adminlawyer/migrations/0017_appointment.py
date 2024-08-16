# Generated by Django 3.2.16 on 2023-03-24 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminlawyer', '0016_delete_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=10)),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.cases')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.client')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
