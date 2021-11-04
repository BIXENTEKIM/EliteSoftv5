from django.db import models

from setups.academics.subjects.models import SchoolSubjects


class SubjectGroups(models.Model):
    sg_code = models.AutoField(primary_key=True)
    subjectgroups_subject = models.ForeignKey(SchoolSubjects, on_delete=models.CASCADE, null=True, blank=True)
    sg_group = models.IntegerField(null=False,blank=False)
    sg_compulsory_f12 = models.BooleanField(default=True,null=False,blank=False)
    sg_compulsory_school = models.BooleanField(default=False,null=False,blank=False)

    class Meta:
        db_table = 'Setups_SubjectGroups'
