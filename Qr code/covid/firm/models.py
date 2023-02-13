from pyexpat import model
from django.db import models
import datetime

# Create your models here.
class Firm(models.Model):
    firmname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    pwd=models.CharField(max_length=30)
    contactno=models.CharField(max_length=15)
    licence=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
class firmstoredata(models.Model):
   # qrdatafirm=models.ImageField(upload_to="qrcode_firm",null=True,blank=True)
    pdf=models.FileField(upload_to="firmpdfdata",null=True,blank=True)
    data=models.CharField(max_length=1000,default="")
    datescanned=models.DateField(default=datetime.date.today())
    firm=models.ForeignKey(Firm,on_delete=models.CASCADE)
class tempqrstore(models.Model):
    qrdata=models.ImageField(upload_to="qrtempcode",null=True,blank=True)
    datescanned=models.DateField(default=datetime.date.today())
    firm=models.ForeignKey(Firm,on_delete=models.CASCADE)

