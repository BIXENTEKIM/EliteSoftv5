# Generated by Django 3.0 on 2021-11-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('document_code', models.AutoField(primary_key=True, serialize=False)),
                ('document_name', models.CharField(blank=True, max_length=200, null=True)),
                ('document_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('document_required', models.BooleanField(default=False)),
            ],
        ),
    ]
