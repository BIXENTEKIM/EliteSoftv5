# Generated by Django 3.0 on 2021-11-18 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20211118_0610'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='students',
            table='student_students',
        ),
    ]