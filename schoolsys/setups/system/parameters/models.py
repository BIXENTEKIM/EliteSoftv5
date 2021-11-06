from django.db import models


class Parameters(models.Model):
    param_code = models.AutoField(primary_key=True)
    param_name = models.CharField(max_length=50)
    param_value=models.CharField(max_length=200)
    param_desc = models.CharField(max_length=500)

    class Meta:
        db_table = 'Setups_Parameters'