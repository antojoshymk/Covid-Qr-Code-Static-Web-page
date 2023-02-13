from django.shortcuts import render,redirect
#from django.urls import get_urlconf
from firm.models import *
from  tkinter import * 
from tkinter import filedialog
import cv2
#import zbar
import os
from firm.utils import render_to_pdf
from io import BytesIO,StringIO
from django.core.files import File
#os.environ['PATH'] += ';C:\\programfiles\\Python39\\scripts'
from django.core.files.storage import FileSystemStorage
from pyzbar.pyzbar import decode
from platform import release
from django.http.response import StreamingHttpResponse
from firm.camera import VideoCamera
#from firm.camera import VideoCamera


# Create your views here.
def firmregister(request):
       
    global pwd1
    
    if request.method=="POST":
        firmname=request.POST.get('firmname')
        email=request.POST.get('email')

        pwd=request.POST.get('pwd')
        pwd1=request.POST.get('pwd1')
        contactno=request.POST.get('contactno')
        licence=request.POST.get('licence')
        location=request.POST.get('location')
        
        # Validation

        error_message=None


        firm_obj=Firm(firmname=firmname,email=email,pwd=pwd,contactno=contactno,location=location,licence=licence)
        error_message =validatefirm(firm_obj)
        if not error_message:
            firm_obj.save()
            return redirect("firmchkadminmsg")
        else:
            data = {
                'error': error_message,
                
            }
            return render(request,"firmregister.html",data)
        
    return render(request,"firmregister.html")
def firmchkadminmsg(request):

    return render(request,"firmchkadminmsg.html")   
        
       
        
          
                   
def validatefirm(firm_obj):
    error_message = None
    p=Firm.objects.filter(email=firm_obj.email)
    if p:
     
        error_message="Email already exist"
    
    elif  (not firm_obj.firmname):
        error_message = "Firm Name Required !!"
    
    elif (firm_obj.pwd) != pwd1:
        error_message = 'Password Do not match'
    elif len(firm_obj.email) < 5:
            error_message = 'Email must be 5 char long'
    
    elif len(firm_obj.contactno) < 10:
            error_message = 'Contact Number must be 10 '
    elif (not firm_obj.licence) :
            error_message = 'Licence number required '
    
    elif not firm_obj.location:
            error_message = 'Location required'
    return error_message

def firmhome(request):
    return render(request,"firmhome.html")
def firmlogin(request):
    
    if request.method =="GET":
        return render(request,"firmlogin.html")
    else:
        flag=0
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        error_message = None
        try:
            
            firm_obj = Firm.objects.get(email=email)
            
            
        except:
                       
            error_message="Firm doen't exist"
            return render(request,"firmlogin.html",{'error':error_message})
        data={'client_obj':firm_obj}
        
        print(data)
        
            
        if firm_obj and firm_obj.status==1 :
            if(pwd==firm_obj.pwd):
                flag=1

    
        
            if flag :
                request.session['id']=firm_obj.id
                request.session['name']=firm_obj.firmname
                return render(request,"firmhome.html",data)
            else:
                error_message = 'Email or Password invalid !!'
                return render(request,"firmlogin.html",{'error':error_message})
        else:
           if firm_obj.status==0:
                    error_message="Admin permission required"
           else:
                              
               error_message = 'Email or Password invalid !!'
        return render(request,"firmlogin.html",{'error':error_message})
    return render(request,"clientlogin.html",{'error':error_message})
def search(request):
    if request.method=="post":
        date=request.post.get("date")
        print("date=",date)
        firmstore_obj=firmstoredata.objects.filter(firm=request.session['id'],datescanned=date)
        print(firmstore_obj)
    
        return render(request,"search.html",{"firmstore_obj":firmstore_obj})
    else:
        print("i am here")
        date=request.GET.get("date")
        print("date=",date)
        firmstore_obj=firmstoredata.objects.filter(firm=request.session['id'],datescanned=date)
        print(firmstore_obj)
    
        return render(request,"search.html",{"firmstore_obj":firmstore_obj,"date":date})

def scanqrcode(request):
    return render(request,"scanqrcode.html")

def scanqr(request):
    return render(request,"scanqr.html")
def scancode(request):
    #file_open =filedialog.askopenfilename(initialdir="D:/",title="select a file")
    if request.method=="POST":
        scan=(request.FILES["scan"])
        #fs=FileSystemStorage()
        #filename=fs.save(scan)
        #uploadurl=fs.url(filename)
        #print("scan=",scan)
        
        d="D:/finalqrcode/finalqr1/new/navya/Qr code/covid"
        #d="C:/Users/NAVYA/Downloads/finalqr/new/navya/Qr code/covid"
        #d="C:/Users/NAVYA/OneDrive/Documents/navya (1)/navya/Qr code/covid"
        data=tempqrstore(qrdata=scan,firm=Firm(request.session['id']))
        data.save()
        print (data)
        try:

            img=cv2.imread(d+data.qrdata.url)
            #print(img)
            #det=cv2.QRCodeDetector()
            print('inside det')
           # print(det.detectAndDecode(img))
            #mydata,s,f=det.detectAndDecode(img)
            print('decode')
        #for barcode in det.detectAndDecode(img):
        #print(barcode)
                #mydata=barcode
            #print(mydata)
            for barcode in decode(img):
                print(barcode.data)
                mydata=barcode.data.decode('utf-8')
                print(mydata)
           
            if mydata:
                firmstoreobj=firmstoredata(data=mydata,firm=Firm(request.session['id']))
                firmstoreobj.save()
                pdf= render_to_pdf(firmstoreobj.id,'qrdata.html', {"mydata":mydata})
                global filename
                filename="qrdata%s.pdf"%(firmstoreobj.id)
                firmstoreobj.pdf.save(filename,File(BytesIO(pdf.content)))
                firmstoreobj.save()
                data={'mydata':mydata,'firmstoreobj':firmstoreobj}
               # data={'mydata':mydata}
                return render(request,"resultvideo.html",data)
        except:
            return render(request,"sorry.html")
        #print(d+data.qrdatafirm)
        '''a=cv2.QRCodeDetector()
        print(d+data.qrdatafirm.url)'''
        #img=cv2.imread(d+data.qrdatafirm.url)
        '''val,points,straight_qrcode=a.detectAndDecode(img)
        print(type(val))'''
        '''for barcode in decode(img):
                print(barcode.data)
                mydata=barcode.data.decode('utf-8')
                print(mydata)
                if mydata:
                    firmstoreobj=firmstoredata(data=mydata,firm=Firm(request.session['id']))
                    firmstoreobj.save()
                    data={'mydata':mydata}
                    return render(request,"result.html",data)'''
                
            

       #
       #     firmstoreobj=firmstoredata(data=val,firm=Firm(request.session['id']))
            #firmstoreobj.save()
            #data={'mydata':val}
            #return render(request,"result.html",data)'''

        

    #img=cv2.imread(scan)
        '''print(val.split())
        k=val.split("\n")
        for i in k:
            print(i)'''
            

        return render(request,"scanqr.html")
    return render(request,"scanqr.html")
def videoscan(request):
    
    cap = cv2.VideoCapture()
# The device number might be 0 or 1 depending on the device and the webcam
    cap.open(0, cv2.CAP_DSHOW)
    while(True):

        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):

            break
    cap.release()
    cv2.destroyAllWindows()
    
    

                   
    return render(request,"scanqr.html")
def logoutfirm(request):
    request.session.clear()
    return redirect('/')    
def sorry(request):
    return render(request,"sorry.html")
def submitpdf_firm(request):
    if request.method=="POST":
        pdf=request.POST.get('pdf')
        obj=firmstoredata(pdf=pdf,firm=Firm(request.session['id']))
        obj.save()
        return render(request,"firmhome.html")

    return render(request,"submitpdf_firm.html")
def videoqrscan(request):

        return render(request,"videoqrscan.html")

'''def gen(camera):

    global mydata
    while True:

        
        frame,mydata= camera.get_frame,()
        if mydata:
            print(mydata)
            break
        else:
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
           
                        
            
    release()    
    cv2.destroyAllWindows()
    return mydata'''
def gen(camera):
    global mydata,s
    while True:


        
        
        frame,mydata= camera.get_frame()
        if mydata:

            print(mydata)

            firmstoreobj=firmstoredata(data=mydata,firm=Firm(s))
            firmstoreobj.save()
            pdf= render_to_pdf(firmstoreobj.id,'qrdata.html', {"mydata":mydata})
            global filename
            filename="qrdata%s.pdf"%(firmstoreobj.id)
            firmstoreobj.pdf.save(filename,File(BytesIO(pdf.content)))
            firmstoreobj.save()
            
            global data
            
            data={'mydata':mydata,'firmstoreobj':firmstoreobj}
            break
            
        else:
            
                        
            yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n') 
    release()    
    cv2.destroyAllWindows()
    return mydata

def resultvideo(request):

        global mydata

        #print(mydata)
        return render(request,"resultvideo.html",{'mydata':mydata})
def video_stream(request):
    global s
    s=request.session['id']
    cam=VideoCamera()
    return StreamingHttpResponse(gen(cam),content_type='multipart/x-mixed-replace; boundary=frame')
