from django.db import models

# Create your models here.
class kartdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to='profile',null=True,blank=True)

class productdb(models.Model):
    Category = models.CharField(max_length=30, null=True, blank=True)
    Productname = models.CharField(max_length=30, null=True, blank=True)
    Quantity = models.IntegerField( null=True, blank=True)
    Description = models.CharField(max_length=300, null=True, blank=True)
    Price = models.IntegerField( null=True, blank=True)
    Image = models.ImageField(upload_to='Products',null=True,blank=True)
