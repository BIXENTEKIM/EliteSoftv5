# Generated by Django 3.0 on 2021-11-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('temp_code', models.AutoField(primary_key=True, serialize=False)),
                ('temp_module', models.CharField(max_length=50)),
                ('temp_name', models.CharField(max_length=200)),
                ('temp_desc', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'Setups_Templates',
            },
        ),
    ]
