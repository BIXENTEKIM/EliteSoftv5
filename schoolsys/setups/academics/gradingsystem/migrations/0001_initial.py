# Generated by Django 3.0 on 2021-12-07 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradesApplicableTo',
            fields=[
                ('applicable_code', models.AutoField(primary_key=True, serialize=False)),
                ('applicable_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GradingSystem',
            fields=[
                ('grading_code', models.AutoField(primary_key=True, serialize=False)),
                ('grading_name', models.CharField(max_length=200)),
                ('points_from', models.CharField(blank=True, max_length=200, null=True)),
                ('points_to', models.CharField(blank=True, max_length=200, null=True)),
                ('grading_grade', models.CharField(blank=True, max_length=200, null=True)),
                ('grading_remarks', models.CharField(blank=True, max_length=400, null=True)),
                ('auto_increment', models.BooleanField(default=False)),
                ('applicable_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gradingsystem.GradesApplicableTo')),
                ('grading_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.Departments')),
            ],
        ),
    ]