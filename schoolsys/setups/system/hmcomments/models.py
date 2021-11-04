from django.db import models



class HMComments(models.Model):
    hm_code = models.AutoField(primary_key=True)
    hm_val1 = models.IntegerField(default=0)
    hm_val2 = models.IntegerField(default=0)
    hm_grade = models.CharField(max_length=20 )
    hm_remarks = models.CharField(max_length=50 )

    class Meta:
        db_table = 'Setups_HMComments'
