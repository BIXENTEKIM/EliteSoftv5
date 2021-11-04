# Generated by Django 3.0 on 2021-11-04 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0003_auto_20211027_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectGroups',
            fields=[
                ('sg_code', models.AutoField(primary_key=True, serialize=False)),
                ('sg_group', models.IntegerField()),
                ('sg_compulsory_f12', models.BooleanField(default=True)),
                ('sg_compulsory_school', models.BooleanField(default=False)),
                ('subjectgroups_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.SchoolSubjects')),
            ],
            options={
                'db_table': 'Setups_SubjectGroups',
            },
        ),
    ]