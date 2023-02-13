from email.mime import image
#from tkinter import _Image
from tkinter.tix import IMAGE, MAX
from django.http import HttpResponse
from django.shortcuts import render,redirect
from client.models import*
from client.utils import render_to_pdf
from io import BytesIO,StringIO
#from pyzbar.pyzbar import decode


from django.core.files import File


from django.core.files.uploadedfile import InMemoryUploadedFile

import cv2
import datetime





import qrcode


# Create your views here.

def clientregister(request):
    global pwd1
    if request.method=="POST":
        clientname=request.POST.get('clientname')
        email=request.POST.get('email')

        pwd=request.POST.get('pwd')
        pwd1=request.POST.get('pwd1')
        contactno=request.POST.get('contactno')
        adhar=request.POST.get('adhar')
        photo=request.FILES['photo']
        #location=request.POST.get('location')
        print(adhar)
        # Validation

        error_message=None


        client_obj=Client(clientname=clientname,email=email,pwd=pwd,contactno=contactno,adhar=adhar,photo=photo)
        error_message =validateclient(client_obj)
        if not error_message:
            client_obj.save()
            return redirect("Clientchkadminmsg")
        else:
            data = {
                'error': error_message,
                
            }
            return render(request,"clientregister.html",data)
        
    return render(request,"clientregister.html")
def Clientchkadminmsg(request):

    return render(request,"clientchkadminmsg.html")   
        
       
        
          
                   
def validateclient(client_obj):
    error_message = None
    p=Client.objects.filter(email=client_obj.email)
    if p:
     
        error_message="Email already exist"
    
    elif  (not client_obj.clientname):
        error_message = "client Name Required !!"
    
    elif (client_obj.pwd) != pwd1:
        error_message = 'Password Do not match'
    elif len(client_obj.email) < 5:
            error_message = 'Email must be 5 char long'
    
    elif len(client_obj.contactno) < 10:
            error_message = 'Contact Number must be 10 '
    elif len(client_obj.adhar) < 12 or len(client_obj.adhar)>12:
            error_message = 'Adhar Number must be 12 '
    
    return error_message
def clientlogin(request):
    flag=0
    
    if request.method =="GET":
        return render(request,"clientlogin.html")
    else:
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        error_message = None
        try:
            
            client_obj = Client.objects.get(email=email)
            
            
        except:
                       
            error_message="Client doen't exist"
            return render(request,"clientlogin.html",{'error':error_message})
        data={'client_obj':client_obj}
        
        print(data)
        
            
        if client_obj and client_obj.status==1 :
            if(pwd==client_obj.pwd):
                flag=1

    
        
            if flag :
                request.session['id']=client_obj.id
                request.session['name']=client_obj.clientname
                return render(request,"clienthome.html",data)
            else:
                error_message = 'Email or Password invalid !!'
                return render(request,"clientlogin.html",{'error':error_message})
        else:
           if client_obj.status==0:
                    error_message="Admin permission required"
           else:
                              
               error_message = 'Email or Password invalid !!'
        return render(request,"clientlogin.html",{'error':error_message})
    return render(request,"clientlogin.html",{'error':error_message})
def clienthome(request):
    return render(request,"clienthome.html")

def clientdatacollect(request):
    if request.method=="GET":
        obj1=Client.objects.get(id=request.session['id'])
        obj=clientdataqrexe2.objects.filter(client=Client(request.session['id']))
        if obj:
            obj=clientdataqrexe2.objects.filter(client=Client(request.session['id'])).order_by('-id')[0]
            print(obj)
        
            print(obj.phone,obj.post,obj.street,obj.first_dose)
            return render(request,"clientdatacollect.html",{'obj':obj,'obj1':obj1})
            
        else:
            print(obj1)
            return render(request,"clientdatacollect.html",{"obj1":obj1})
    if request.method=="POST":
        #symptoms=request.POST.getlist("chk[]")
        hadcovid19=request.POST.get('hadcovid19')
        coviddate=request.POST.get('coviddate')
        print("coviddate=",coviddate)
        if not coviddate:
            coviddate=None
        print(coviddate)
        vaccinated=request.POST.get('vaccinated')
        first_dose=request.POST.get('firstdose')
        if not first_dose:
            first_dose=None
        
        second_dose=request.POST.get('seconddose')
        if not second_dose:
            second_dose=None
        
        contact_covid=request.POST.get('contact_covid')
        contact_date=request.POST.get('contact_date')
        if not contact_date:
            contact_date=None
        
        print(contact_date)
        reference=request.POST.get('reference')
        passanger=request.POST.get('passanger')
        covid_test=request.POST.get('covid_test')
        street=request.POST.get('street')
        city=request.POST.get('city')
        country=request.POST.get('country')
        email=request.POST.get('email')
        phone=request.POST.get('phone')

        post=request.POST.get('post')
        
        print(contact_date)

        obj=clientdataqrexe2(hadcovid19=hadcovid19,coviddate=coviddate,vaccinated=vaccinated,first_dose=first_dose,second_dose=second_dose,contact_covid=contact_covid,passanger=passanger,covid_test=covid_test,cotact_date=contact_date,street=street,city=city,country=country,post=post,email=email,phone=phone,todaydate=datetime.date.today(),client=Client(request.session['id']),reference=reference)
        obj.save()
        name=Client.objects.filter(id=request.session['id'])
        for i in name:
            print(i.clientname)
        global pdf
        pdf= render_to_pdf(obj.id,'certificate.html', {'obj':obj,'name':name})
        document=clientdocument(client=clientdataqrexe2(obj.id))
        global filename
        filename="test%s.pdf"%(obj.id)
        document.pdfdata.save(filename,File(BytesIO(pdf.content)))
        document.save()
        name=request.session['name']
        if second_dose==None:
            second_dose="Not selected"
        if coviddate==None:
            coviddate="Covid Not affected"
        if contact_date==None:
            contact_date="No Contact with Covid Patients"
        d=datetime.date.today()

        '''img=qrcode.make("QR Code Created Date:%s\n\nName:'%s'\n\nContact No:'%s'\n\nEmail Address:'%s'\n\nAddress:\n\nStreet:%s\n\nLocation:%s\n\nPinCode:%s\n\nCowin Reference ID:%s\n\nVaccinated:%s\n\nFirst Dose Date:'%s'\n\nSecond Dose Date:%s\n\n symptoms Now:%s\n\nHadcovid Before:%s\n\nCovid Affected Time Period:%s\n\nAny contact with Covid Patients:%s\n\nTime period:%s\n\nDid Any Covid Test within 48hours:%s "%(str(d),str(name),str(phone),str(email),str(street),str(city),str(post),str(reference),str(vaccinated),str(first_dose),str(second_dose),str(symptoms),str(hadcovid19),str(coviddate),str(contact_covid),str(contact_date),str(covid_test)))
        img1=qrcode.make("Name:'%s'\nContact No:'%s'\nCowin Reference ID:'%s'"%(str(name),str(phone),str(reference)))
        imgfile="img%s.jpg"%(obj.id)
        img.save(imgfile)

        buffer=BytesIO()
        img.save(buffer,'PNG')
        imgfilevideo="imgvid%s.jpg"%(obj.id)
        img1.save(imgfilevideo)
        buffer=BytesIO()
        img1.save(buffer,'PNG')

        


        document.qrdata.save(imgfile,File(buffer))
        document.qrvideo.save(imgfilevideo,File(buffer))'''

        # upload qr code creation
        img=qrcode.make("QR Code Created Date:%s\n\nName:'%s'\n\nContact No:'%s'\n\nEmail Address:'%s'\n\nAddress:\n\nStreet:%s\n\nLocation:%s\n\nPinCode:%s\n\nCowin Reference ID:%s\n\nVaccinated:%s\n\nFirst Dose Date:'%s'\n\nSecond Dose Date:%s\n\n Hadcovid Before:%s\n\nCovid Affected Time Period:%s\n\nAny contact with Covid Patients:%s\n\nTime period:%s\n\nDid Any Covid Test within 48hours:%s "%(str(d),str(name),str(phone),str(email),str(street),str(city),str(post),str(reference),str(vaccinated),str(first_dose),str(second_dose),str(hadcovid19),str(coviddate),str(contact_covid),str(contact_date),str(covid_test)))
        imgfile="img%s.jpg"%(obj.id)
        img.save(imgfile)

        buffer=BytesIO()
        img.save(buffer,'PNG')
        document.qrdata.save(imgfile,File(buffer))

        #video qr code creation
        '''img1=qrcode.make("Name:'%s'\nContact No:'%s'\nCowin Reference ID:'%s'"%(str(name),str(phone),str(reference)))
        imgfilevideo="imgvid%s.jpg"%(obj.id)
        img1.save(imgfilevideo)
        buffer=BytesIO()
        img1.save(buffer,'PNG')
        document.qrvideo.save(imgfilevideo,File(buffer))'''








        #document.qrdata.save(imgfile,image()))
        #image1=img.make_image()
        #document=clientdocument(qrdata=img)
        #print(img)
        #document.qrdata.save(imgfile,img.url)
        #document.save()


        
        
        
        #name=Client.objects.filter(id=request.session['id'])
        #data={'obj':obj,'name':name}
        #return render(request,"certificate.html",data)
    #return render(request,"clienthome.html")

        return render(request,"downloadpdf.html",{'document':document,})
def downloadpdf(request):
    if request.method=="POST":
        scan=request.Files('photo')
        a=cv2.QRCodeDetector()
        val,points,straight_qrcode=a.detectAndDecode(cv2.imread(scan))
        

    return render(request,"downloadpdf.html")
def logoutclient(request):
    request.session.clear()
    return redirect('/')    
