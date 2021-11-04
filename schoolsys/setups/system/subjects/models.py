from django.db import models

from setups.academics.departments.models import SchoolDepartments


class SchoolSubjects(models.Model):
    subject_code = models.AutoField(primary_key=True)
    subject_sht_code = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=200)
    subject_order = models.IntegerField(default=0)
    subject_department = models.ForeignKey(SchoolDepartments, on_delete=models.CASCADE, null=True, blank=True)
    subject_full = models.BooleanField(default=True, null=True, blank=True)
    subject_main = models.BooleanField(default=True, null=True, blank=True)
    subject_pct = models.IntegerField(default=0, null=True, blank=True)
    subject_comb_name = models.CharField(max_length=200,null=True,blank=True)
    subject_level = models.IntegerField(default=0, null=True, blank=True)
    subject_multiply_by = models.IntegerField(default=0, null=True, blank=True)
    subject_include_for_pos = models.BooleanField(default=True)
    subject_combined = models.BooleanField(default=False, null=True, blank=True)
    subject_gradable = models.BooleanField(default=True, null=True, blank=True)
