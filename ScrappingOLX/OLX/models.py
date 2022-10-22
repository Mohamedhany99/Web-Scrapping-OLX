from django.db import models

# Create your models here.
class Items(models.Model):
    _id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=1000,default='None')
    name=models.CharField(max_length=1000)
    price = models.FloatField()