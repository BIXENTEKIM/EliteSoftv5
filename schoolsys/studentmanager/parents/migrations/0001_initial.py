# Generated by Django 3.0 on 2021-11-16 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proffessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel')),
            ],
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('parent_code', models.AutoField(primary_key=True, serialize=False)),
                ('father_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=200, null=True)),
                ('father_address', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_address', models.CharField(blank=True, max_length=200, null=True)),
                ('id_no', models.CharField(blank=True, max_length=200, null=True)),
                ('father_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('father_email', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_email', models.CharField(blank=True, max_length=200, null=True)),
                ('parent_type', models.CharField(blank=True, max_length=200, null=True)),
                ('email_required', models.BooleanField(default=True)),
                ('parent_photo', models.ImageField(blank=True, null=True, upload_to='parent_pics')),
                ('father_proffession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father_proffession_foreignkey', to='proffessions.Proffessions')),
                ('mother_proffession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mother_proffession_foreignkey', to='proffessions.Proffessions')),
            ],
        ),
    ]
