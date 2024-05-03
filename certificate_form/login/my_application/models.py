from django.db import models

# Create your models here.
class certificate_form(models.Model):
    reg_no=models.CharField(max_length=10,default="")
    name=models.CharField(max_length=20,default="")
    email=models.CharField(max_length=20,default="")
    course=models.CharField(max_length=20,default="")
    trainer=models.CharField(max_length=15,default="")
    phone=models.IntegerField(default="")