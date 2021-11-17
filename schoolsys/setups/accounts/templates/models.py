from django.db import models


class Templates(models.Model):
    temp_code = models.AutoField(primary_key=True)
    temp_module = models.CharField(max_length=50)
    temp_name=models.CharField(max_length=200)
    temp_desc = models.CharField(max_length=500)

    class Meta:
        db_table = 'Setups_Templates'