# Generated by Django 4.2.4 on 2023-09-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operat', '0002_alter_appuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]