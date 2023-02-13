from django.urls import path
from client import views

urlpatterns=[
    path("clientregister",views.clientregister,name="clientregister"),
    path("Clientchkadminmsg",views.Clientchkadminmsg,name="Clientchkadminmsg"),
    path("clientlogin",views.clientlogin,name="clientlogin"),
    path("clienthome",views.clienthome,name="clienthome"),
    path("clientdatacollect",views.clientdatacollect,name="clientdatacollect"),
    path("logoutclient",views.logoutclient,name="logouclient"),

]