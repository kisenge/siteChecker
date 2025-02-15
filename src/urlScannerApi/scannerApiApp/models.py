from django.db import models
import json

# Create your models here.
class Data(models.Model):
    url= models.CharField(max_length=500)
    taskId= models.CharField(max-length=100,null=True,blank=True)
    status= models.CharField(max_length=50,default='pending')
    result= models.JSONField(null=True,blank=True)
