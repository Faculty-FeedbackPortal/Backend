# Generated by Django 4.2.4 on 2023-11-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anony', '0003_remove_practical_feedback_attendence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practical_feedback',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='theory_feedback',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
