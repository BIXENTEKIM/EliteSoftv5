from django.db import models


class SchoolDepartments(models.Model):
    dp_code = models.AutoField(primary_key=True)
    dp_sht_name = models.CharField(max_length=4)
    dp_name = models.CharField(max_length=200)
    dp_sequence = models.CharField(max_length=20)