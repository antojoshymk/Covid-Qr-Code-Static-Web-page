

# Create your views here.
from django.shortcuts import render,redirect
from client.models import *
from firm.models import *
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
def Adminlogin(request):
       
    if request.method =="GET":
        return render(request,"adminlogin.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message=None
        print(email,password)
        if email=="admin@gmail.com" and password=="admin@123":
           return render(request,"Adminhome.html")
        else:
            error_message="invalid"
            return render(request,"adminlogin.html",{'error':error_message})
    #return render(request,"adminlogin.html")
def Adminhome(request):
    if request.method=="GET":
        return render(request,"Adminhome.html")
    return redirect(request,"Adminhome.html")  
def approveclient(request):
    if request.method=="GET":
        client_obj=Client.objects.all()
        return render(request,"approveclient.html",{'client_obj':client_obj})
def approvefirm(request):
    if request.method=="GET":
        firm_obj=Firm.objects.all()
        return render(request,"approvefirm.html",{'firm_obj':firm_obj})
def firmapproval(request,pk):
    if request.method=="GET":
        print("inside get")
        firm_obj=Firm.objects.filter(id=pk)#.update(status=True)
        for i in firm_obj:
            i.status=True
            mail=i.email
            i.save()
        email_obj=EmailMessage('Approved your Account','Hi...Your registeration Approved by Admin ',settings.EMAIL_HOST_USER,[mail,])
        email_obj.send()        
        print("Approved")
    
        book_obj=Firm.objects.all()
        return render(request,"approvefirm.html",{'firm_obj':firm_obj})
def firmdecline(request,pk):
    #user_tb.objects.filter(id=pk).update(status=False)
    if request.method=="GET":
        firm_obj=Firm.objects.filter(id=pk)#.update(status=True)
        for i in firm_obj:
            i.status=False
            i.save()
        firm_obj=Firm.objects.all()
        print(firm_obj)
        return render(request,"approvefirm.html",{'firm_obj':firm_obj})    
def logoutadmin(request):
    return redirect("/")




def clientapproval(request,pk):
    if request.method=="GET":
        print("inside get")
        client_obj=Client.objects.filter(id=pk)#.update(status=True)
        for i in client_obj:
            i.status=True
            mail=i.email
            i.save()
        email_obj=EmailMessage('Approved your Account','Hi...Your registeration Approved by Admin ',settings.EMAIL_HOST_USER,[mail,])
        email_obj.send()        
        print("Approved")
    
        client_obj=Client.objects.all()
        return render(request,"approveclient.html",{'client_obj':client_obj})
def clientdecline(request,pk):
    #user_tb.objects.filter(id=pk).update(status=False)
    if request.method=="GET":
        client_obj=Client.objects.filter(id=pk)#.update(status=True)
        for i in client_obj:
            i.status=False
            i.save()
        client_obj=Client.objects.all()
        print(client_obj)
        return render(request,"approveclient.html",{'client_obj':client_obj})    
