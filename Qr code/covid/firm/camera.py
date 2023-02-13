from urllib import response
from django.shortcuts import render,redirect
from django.http.response import StreamingHttpResponse
from django.http import HttpResponse, request
from pyzbar.pyzbar import decode


import cv2
#from pyzbar.pyzbar import decode
import numpy as np
global mydata
mydata=0
class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    def __del__(self):
        self.cap.release()
    def get_frame(self):
        global mydata
        mydata=None
        ret, frame = self.cap.read()
        try:
            #det=cv2.QRCodeDetector()
            #mydata,s,y=det.detectAndDecode(frame)
            #print(mydata)

            for barcode in decode(frame):
               print(barcode.data)
               mydata=barcode.data.decode('utf-8')
               print(mydata)
        except:

            if mydata:
                return frame,mydata
            
           
            
                             
            
            
        

        frame_flip = cv2.flip(frame, 1)
        ret, frame = cv2.imencode('.jpg', frame_flip)
        
        return frame.tobytes(),mydata