# Generated by Django 3.0 on 2021-11-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20211117_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='status',
            field=models.CharField(default='Active', max_length=200),
        ),
    ]
