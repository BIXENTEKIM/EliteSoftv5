# Generated by Django 3.0 on 2021-11-17 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmaster', '0007_auto_20211116_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmaster',
            name='am_account_no',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
