from django.db import models



class Organisation(models.Model):
    org_code = models.AutoField(primary_key=True)
    Org_Name  = models.CharField(max_length=100,null=False,blank=False)
    Org_Physical_Address = models.CharField(max_length=200,null=False,blank=False)
    Org_Tel_No = models.CharField(max_length=30,null=False,blank=False)
    Org_Logo = models.ImageField(upload_to='Org_Logo',null=True,blank=True)
    Org_Email = models.CharField(max_length=100,null=False,blank=False)
    Org_Website = models.CharField(max_length=100, null=False, blank=False)
    Org_Tag_Line  = models.CharField(max_length=200,null=False,blank=False)
    Org_Poastal_Address = models.CharField(max_length=200,null=False,blank=False)
    Org_Type = models.CharField(max_length=200,null=True,blank=True,default=1)#1 is secondary, 2 is primary, 3 is tertially,4 is payroll
    Org_Logo2 = models.ImageField(upload_to='Org_Logo2',null=True,blank=True)
    Org_Cell_No = models.CharField(max_length=30,null=False,blank=False)
    Org_Mission = models.CharField(max_length=200,null=True,blank=True)
    Org_Vision = models.CharField(max_length=200,null=True,blank=True)
    Org_Pin_No = models.CharField(max_length=11,null=True,blank=True)
    Org_NHIF_Code= models.CharField(max_length=30,null=True,blank=True)
    Org_NSSF_Code= models.CharField(max_length=30,null=True,blank=True)

    class Meta:
        db_table = 'Setups_Organisation'
