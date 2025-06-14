# Generated by Django 5.2.1 on 2025-05-11 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_nm', models.IntegerField(unique=True)),
                ('sname', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=11)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.college')),
            ],
        ),
    ]
