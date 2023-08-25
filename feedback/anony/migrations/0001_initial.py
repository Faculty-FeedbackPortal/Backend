# Generated by Django 4.2.4 on 2023-08-23 13:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theory_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=5)),
                ('batch', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('f_date', models.DateField(default=datetime.date.today)),
                ('attendence', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operat.faculty')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operat.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Practical_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=5)),
                ('batch', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('f_date', models.DateField(default=datetime.date.today)),
                ('attendence', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operat.faculty')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operat.subjects')),
            ],
        ),
    ]
