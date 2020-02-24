from django.db import models

# Create your models here.
class Admin(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
class Merchant(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    contactno=models.IntegerField()
    emailid=models.EmailField(unique=True)
    password=models.CharField(max_length=30)
class Product(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    price=models.FloatField()
    quantity=models.IntegerField()
    mid=models.ForeignKey(Merchant,on_delete=models.CASCADE,default=False)
    # place = models.OneToOneField(PlaceModel, on_delete=models.CASCADE, default=False)
    # type_of_biryani = models.ForeignKey(BiryaniTypes, on_delete=models.CASCADE)

