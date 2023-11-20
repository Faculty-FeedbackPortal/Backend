# Generated by Django 4.2.4 on 2023-11-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anony', '0002_studentuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practical_feedback',
            name='attendence',
        ),
        migrations.RemoveField(
            model_name='theory_feedback',
            name='attendence',
        ),
        migrations.AddField(
            model_name='practical_feedback',
            name='attendance',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='theory_feedback',
            name='attendance',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
