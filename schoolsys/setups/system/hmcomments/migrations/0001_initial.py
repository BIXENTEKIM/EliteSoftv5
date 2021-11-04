# Generated by Django 3.0 on 2021-11-03 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HMComments',
            fields=[
                ('hm_code', models.AutoField(primary_key=True, serialize=False)),
                ('hm_val1', models.IntegerField(default=0)),
                ('hm_val2', models.IntegerField(default=0)),
                ('hm_grade', models.CharField(max_length=20)),
                ('hm_remarks', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Setups_HMComments',
            },
        ),
    ]
