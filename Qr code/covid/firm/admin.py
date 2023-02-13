#from django.contrib import admin

# Register your models here.
#from firm.models import *
#admin.site.register(Firm)
from argparse import Action
import email

from django.contrib import admin

# Register your models here.
from firm.models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string






class Firmstatus(admin.ModelAdmin):
    model=Firm
    fields=['firmname','email','pwd','contactno','licence','location','status']
    actions=['approvefirm']
    def approvefirm(self,request,queryset):
        queryset.update(status=True)
        id1 = request.POST.get('_selected_action')
        print(id1)
        obj=Firm.objects.filter(id=id1)
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
        email_obj=EmailMessage('Approved your Account','Hi...Your Account QR Code Account Approved by Admin ',settings.EMAIL_HOST_USER,[clientemail,])
        email_obj.send()        
        print("Approved")
    
admin.site.register(Firm,Firmstatus)