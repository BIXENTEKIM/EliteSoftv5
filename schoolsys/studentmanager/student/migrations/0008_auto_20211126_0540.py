# Generated by Django 3.0 on 2021-11-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20211118_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='created_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='created_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
