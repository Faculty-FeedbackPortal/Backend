# Generated by Django 4.2.4 on 2023-10-31 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anony', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]