# Generated by Django 5.2.1 on 2025-05-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_register_lastname_alter_register_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='gender',
            field=models.CharField(default=None, max_length=11),
        ),
    ]
