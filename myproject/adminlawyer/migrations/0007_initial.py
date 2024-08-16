# Generated by Django 3.2.16 on 2023-03-16 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminlawyer', '0006_auto_20230316_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('fir_copy', models.CharField(max_length=255)),
                ('police_station', models.CharField(max_length=255)),
                ('case_type', models.CharField(max_length=50)),
                ('case_reg_date', models.DateField()),
                ('court', models.CharField(max_length=50)),
                ('judge', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'cases',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.BigIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.city')),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'state',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_hearing_date', models.DateField()),
                ('remarks', models.TextField()),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.cases')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lawyer_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.BigIntegerField()),
                ('qualification', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('registration_date', models.DateField()),
                ('address', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'lawyer',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.TextField()),
                ('rating', models.IntegerField()),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.cases')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.client')),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.lawyer')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('document', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.cases')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.client')),
            ],
            options={
                'db_table': 'documents',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.state'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.state'),
        ),
        migrations.AddField(
            model_name='cases',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.city'),
        ),
        migrations.AddField(
            model_name='cases',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.client'),
        ),
        migrations.AddField(
            model_name='cases',
            name='lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.lawyer'),
        ),
        migrations.AddField(
            model_name='cases',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.state'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.client')),
                ('lawyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminlawyer.lawyer')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
