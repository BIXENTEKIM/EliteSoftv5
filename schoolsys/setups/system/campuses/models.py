from django.db import models

from students.models import Counties


class SchoolCampuses(models.Model):
    campus_code = models.AutoField(primary_key=True)
    campus_name = models.CharField(max_length=100)
    campus_location = models.CharField(max_length=200)
    campus_incharge = models.CharField(max_length=70)
    campus_incharge_contacts = models.CharField(max_length=50)
    campus_county= models.ForeignKey(Counties, on_delete=models.CASCADE, null=True, blank=True)
