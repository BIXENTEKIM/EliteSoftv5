# Generated by Django 3.0 on 2021-10-23 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClasses',
            fields=[
                ('class_code', models.AutoField(primary_key=True, serialize=False)),
                ('form', models.CharField(max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('max_capacity', models.IntegerField(default=0)),
                ('admno_prefix', models.CharField(max_length=200)),
                ('class_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teachers')),
                ('next_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.SchoolClasses')),
            ],
        ),
    ]
