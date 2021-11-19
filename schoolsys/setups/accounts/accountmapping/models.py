from django.db import models
from setups.accounts.accountmaster.models import AccountMaster
from setups.accounts.accountmaster.models import AccountMaster as AccountMaster2



class AccountMapping(models.Model):
    acm_code = models.AutoField(primary_key=True)
    acm_type = models.CharField(max_length=100, null=False, blank=False)
    acm_AccountMaster = models.ForeignKey(AccountMaster, on_delete=models.CASCADE, null=False, blank=False,related_name='acm_AccountMaster')
    acm_contra_AccountMaster = models.ForeignKey(AccountMaster2, on_delete=models.CASCADE, null=False, blank=False,related_name='acm_contra_AccountMaster')
    acm_desc = models.CharField(max_length=100, null=False, blank=False)
    acm_created_by = models.CharField(max_length=200, null=True, blank=True)
    acm_created_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'account_mapping'