# Generated by Django 3.0 on 2021-11-09 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_organisation_org_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='Org_Logo',
            field=models.ImageField(blank=True, null=True, upload_to='Org_Logo'),
        ),
    ]
