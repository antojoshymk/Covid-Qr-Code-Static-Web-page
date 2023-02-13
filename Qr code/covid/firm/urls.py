from django.urls import path
from firm import views

urlpatterns=[
    path("firmregister",views.firmregister,name="firmregister"),
    path("firmchkadminmsg",views.firmchkadminmsg,name="firmchkadminmsg"),
    path("firmhome",views.firmhome,name="firmhome"),
    path("firmlogin",views.firmlogin,name="firmlogin"),
    path("scanqr",views.scanqr,name="scanqr"),
    path("scancode",views.scancode,name="scancode"),
    path("videoscan",views.videoscan,name="videoscan"),
    path("logoutfirm",views.logoutfirm,name="logoutfirm"),
    path("sorry",views.sorry,name="sorry"),
    path("submitpdf_firm",views.submitpdf_firm,name="submitpdf_firm"),
    path("videoqrscan",views.videoqrscan,name="videoqrscan"),
    path("video_stream",views.video_stream,name="video_stream"),
    path("resultvideo",views.resultvideo,name="resultvideo"),
    path("search",views.search,name="search"),
    path("scanqrcode",views.scanqrcode,name="scanqrcode"),
    
]