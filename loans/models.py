from django.db import models
 
class Equipment(models.Model):
    invnumber = models.IntegerField()
    category = models.CharField(max_length=10)
    description = models.CharField(max_length=225)
    condition = models.CharField(max_length=225)
    checkedout = models.BooleanField()

class Loans(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zip = models.IntegerField()
    email = models.CharField(max_length=50, default="")
    date_out = models.DateField()
    date_in = models.DateField(blank=True, null=True)
    equip_id = models.IntegerField()
    
    
    