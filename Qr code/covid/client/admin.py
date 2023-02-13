#from django.contrib import admin

# Register your models here.
#from client.models import Client
#admin.site.register(Client)

from argparse import Action
import email
from http import client

from django.contrib import admin

# Register your models here.
from client.models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string






class Clientstatus(admin.ModelAdmin):
    model=Client
    fields=['clientname','email','pwd','contactno','adhar','photo','status']
    actions=['approveclient']
    def approveclient(self,request,queryset):
        queryset.update(status=True)
        id1 = request.POST.get('_selected_action')
        print(id1)
        obj=Client.objects.filter(id=id1)
        print(obj)
        for i in obj:
            clientemail=i.email

        #obj=Firmstatus.get_object()
        #print("obj=",obj)
        #queryset.select(email)
        #print(email)
        
        #print(emailval)
        '''obj=Firm.objects.filter(id=Firmstatus.actions._getitem_(email))
        emailval=obj._getitem_(email)
        print(emailval)'''
        email_obj=EmailMessage('Approved your Account','Hi...Your registeration Approved by Admin ',settings.EMAIL_HOST_USER,[clientemail,])
        email_obj.send()        
        print("Approved")
    
admin.site.register(Client,Clientstatus)