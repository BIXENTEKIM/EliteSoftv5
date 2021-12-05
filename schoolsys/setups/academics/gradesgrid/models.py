from django.db import models

from setups.academics.departments.models import Departments


class GradesGrid(models.Model):
    grades_code = models.AutoField(primary_key=True)
    grades_val1 = models.IntegerField(default=0)
    grades_val2 = models.IntegerField(default=0)
    grades_grade = models.CharField(max_length=20 )
    grades_remarks = models.CharField(max_length=50 )
    grades_department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=False, blank=False)
    grades_option = models.CharField(max_length=50,null=True,blank=True,default="ALL" )
