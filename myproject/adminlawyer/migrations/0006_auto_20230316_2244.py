# Generated by Django 3.2.16 on 2023-03-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminlawyer', '0005_alter_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cases',
            name='city',
        ),
        migrations.RemoveField(
            model_name='cases',
            name='client',
        ),
        migrations.RemoveField(
            model_name='cases',
            name='lawyer',
        ),
        migrations.RemoveField(
            model_name='cases',
            name='state',
        ),
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='client',
            name='city',
        ),
        migrations.RemoveField(
            model_name='client',
            name='state',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='cases',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='client',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='cases',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='client',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='lawyer',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='cases',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Cases',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Lawyer',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
