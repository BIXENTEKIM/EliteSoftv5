from django.db import models


class MasterSetups(models.Model):
    ms_code = models.AutoField(primary_key=True)
    ms_desc = models.CharField(max_length=200)
    ms_type = models.CharField(max_length=100)


    class Meta:
        db_table = 'Setups_MasterSetups'