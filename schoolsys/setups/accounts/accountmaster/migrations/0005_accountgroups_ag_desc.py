# Generated by Django 3.0 on 2021-11-16 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmaster', '0004_remove_accountmaster_am_ie'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountgroups',
            name='ag_desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]