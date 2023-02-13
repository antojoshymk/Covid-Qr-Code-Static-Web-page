from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    #path('',views.index,name="index"),
    path("",views.temp1,name="temp1"),
    path("base",views.base,name="base"),
   
]
