# Generated by Django 3.0 on 2021-12-17 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feesetup', '0002_auto_20211217_1624'),
        ('setups', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StandardCharges',
        ),
    ]
