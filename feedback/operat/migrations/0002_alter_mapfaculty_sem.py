# Generated by Django 4.2.4 on 2023-09-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapfaculty',
            name='sem',
            field=models.IntegerField(null=True),
        ),
    ]
