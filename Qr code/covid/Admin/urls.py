from django.urls import path
from Admin import views

urlpatterns = [
    path("Adminlogin",views.Adminlogin,name="Adminlogin"),
    path("Adminhome",views.Adminhome,name="Adminhome"),
    path("approveclient",views.approveclient,name="approveclient"),
    path("clientapproval<str:pk>",views.clientapproval,name="clientapproval"),
    path("clientdecline<str:pk>",views.clientdecline,name="clientdecline"),
    path("approvefirm",views.approvefirm,name="approvefirm"),
    path("firmapproval<str:pk>",views.firmapproval,name="firmapproval"),
    path("firmdecline<str:pk>",views.firmdecline,name="firmdecline"),
    path("logoutadmin",views.logoutadmin,name="logoutadmin")



    
]
