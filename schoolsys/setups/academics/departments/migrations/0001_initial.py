# Generated by Django 3.0 on 2021-11-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dp_code', models.AutoField(primary_key=True, serialize=False)),
                ('dp_name', models.CharField(max_length=200)),
                ('dp_short_desc', models.CharField(max_length=200)),
                ('seq_desc', models.CharField(max_length=200)),
            ],
        ),
    ]
