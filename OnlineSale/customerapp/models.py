from django.db import models

# Create your models here.
class CustomerDetails1(models.Model):
    cid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(default=False)
    password=models.CharField(max_length=30)
    address=models.TextField(max_length=100)
    status=models.CharField(max_length=30)
    otp=models.IntegerField(default=False)