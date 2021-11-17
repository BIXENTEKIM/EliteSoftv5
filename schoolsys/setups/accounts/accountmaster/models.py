from django.db import models


class AccountTypes(models.Model):
    ac_code = models.AutoField(primary_key=True)
    ac_desc = models.CharField(max_length=100,null=False,blank=False)

    class Meta:
        db_table = 'account_types'


class AccountGroups(models.Model):
    ag_code = models.AutoField(primary_key=True)
    ag_prefix = models.CharField(max_length=20, null=False, blank=False)
    ag_desc = models.CharField(max_length=100, null=True, blank=True)
    ag_AccountTypes = models.ForeignKey(AccountTypes, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'account_groups'


class AccountMain(models.Model):
    ama_code = models.AutoField(primary_key=True)
    ama_desc = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'account_main'


class AccountMaster(models.Model):
    am_code = models.AutoField(primary_key=True)
    am_desc = models.CharField(max_length=200,null=False,blank=False)
    am_AccountGroups = models.ForeignKey(AccountGroups, on_delete=models.CASCADE, null=False, blank=False)
    am_AccountMain = models.ForeignKey(AccountMain, on_delete=models.CASCADE, null=False, blank=False)
    am_status = models.CharField(max_length=10,null=False,blank=False)
    am_account_no = models.CharField(max_length=50,null=True,blank=True,unique=True)
    am_cb = models.BooleanField(default=False,null=False,blank=False)
    am_bs = models.BooleanField(default=False, null=False, blank=False)
    am_pl = models.BooleanField(default=False, null=False, blank=False)
    am_pc = models.BooleanField(default=False, null=False, blank=False)
    am_order = models.IntegerField(default=0 ,null=True, blank=True)
    am_created_by = models.CharField(max_length=200,null=True,blank=True)
    am_created_on = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = 'account_master'
