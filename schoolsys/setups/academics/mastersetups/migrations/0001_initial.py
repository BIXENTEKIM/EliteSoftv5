# Generated by Django 3.0 on 2021-11-02 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasterSetups',
            fields=[
                ('ms_code', models.AutoField(primary_key=True, serialize=False)),
                ('ms_desc', models.CharField(max_length=200)),
                ('ms_type', models.CharField(max_length=10)),
            ],
        ),
    ]
