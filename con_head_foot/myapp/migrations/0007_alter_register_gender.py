# Generated by Django 5.2.1 on 2025-05-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
