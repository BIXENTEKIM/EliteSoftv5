# Generated by Django 3.0 on 2021-11-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_students_stud_active_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='stud_active_status',
            field=models.CharField(blank=True, default='Active', max_length=200, null=True),
        ),
    ]