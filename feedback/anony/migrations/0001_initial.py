# Generated by Django 4.2.4 on 2023-09-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practical_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=5)),
                ('batch', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('f_date', models.IntegerField(default=2023)),
                ('attendence', models.CharField(max_length=30)),
                ('Q1', models.IntegerField(null=True)),
                ('Q2', models.IntegerField(null=True)),
                ('Q3', models.IntegerField(null=True)),
                ('Q4', models.IntegerField(null=True)),
                ('Q5', models.IntegerField(null=True)),
                ('Q6', models.IntegerField(null=True)),
                ('Q7', models.IntegerField(null=True)),
                ('Q8', models.IntegerField(null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Theory_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('division', models.CharField(max_length=5)),
                ('batch', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('f_date', models.IntegerField(default=2023)),
                ('attendence', models.CharField(max_length=30)),
                ('Q1', models.IntegerField(null=True)),
                ('Q2', models.IntegerField(null=True)),
                ('Q3', models.IntegerField(null=True)),
                ('Q4', models.IntegerField(null=True)),
                ('Q5', models.IntegerField(null=True)),
                ('Q6', models.IntegerField(null=True)),
                ('Q7', models.IntegerField(null=True)),
                ('Q8', models.IntegerField(null=True)),
                ('Q9', models.IntegerField(null=True)),
                ('Q10', models.IntegerField(null=True)),
                ('Q11', models.IntegerField(null=True)),
                ('Q12', models.IntegerField(null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=35)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
    ]
