from django.db import models
import datetime

class Client(models.Model):
    clientname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    pwd=models.CharField(max_length=30)
    contactno=models.CharField(max_length=15)
    adhar=models.CharField(max_length=12,default=
    '000000000000')
    photo=models.ImageField(upload_to="client_data")
    status=models.BooleanField(default=False)
class clientdataqrexe2(models.Model):
    #symptoms=models.TextField(default=None, null=True)
    hadcovid19=models.CharField(max_length=5)
    coviddate=models.DateField(null=True,blank=True,default=None)
    vaccinated=models.CharField(max_length=5)
    first_dose=models.DateField(null=True,blank=True)
    second_dose=models.DateField(null=True,blank=True)
    contact_covid=models.CharField(max_length=5)
    cotact_date=models.DateField(null=True,blank=True)
    passanger=models.CharField(max_length=5)
    covid_test=models.CharField(max_length=5)
    street=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=30)
    reference=models.CharField(max_length=30,default='')
    todaydate=models.DateField(default=datetime.date.today())
    status=models.BooleanField(default=False)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
class clientdocument(models.Model):
    pdfdata=models.FileField(upload_to="documents",null=True,blank=True)
    qrdata=models.ImageField(upload_to="qrcode",null=True,blank=True)
    #qrvideo=models.ImageField(upload_to="qrvideodata",null=True,blank=True)
    client=models.ForeignKey(clientdataqrexe2,on_delete=models.CASCADE)




# Create your models here.
