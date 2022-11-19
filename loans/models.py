from django.db import models
 
class Equipment(models.Model):
 invnumber = models.IntegerField()
 category = models.CharField(max_length=10)
 description = models.CharField(max_length=225)
 condition = models.CharField(max_length=225)
 checkedout = models.CharField(max_length=10)
