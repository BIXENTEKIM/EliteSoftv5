from django.db import models

class UserType(models.Model):
    type_code = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=200)
    type_desc = models.CharField(max_length=200)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_firstname = models.CharField(max_length=200)
    user_lastname = models.CharField(max_length=200)
    user_username = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_phone = models.CharField(max_length=200)
    user_address = models.CharField(max_length=200)
    user_gender = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_type= models.ForeignKey(UserType, on_delete=models.CASCADE,null=True)
    user_supervisor= models.ForeignKey("self", on_delete=models.CASCADE,null=True)

