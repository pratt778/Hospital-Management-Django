"""
URL configuration for HospitalManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('contact',Contact,name="contact"),
    path('about',About,name="about"),
    path('adminlogin',adminLogin,name='adlogin'),
    path('adminlogout',adlogout,name='logout'),
    path('admindash',admindash,name='admindash'),
    path('viewdoctor',viewdoctor,name='viewdoctor'),
    path('viewpatient',viewpatient,name='viewpatient'),
    path('viewappoint',viewappoint,name='viewappoint'),
    path('adddoctor',adddoctor,name="adddoctor"),
    path('addpatient',addpatient,name='addpatient'),
    path('addappoint',addappoint,name='addappoint'),
    path('editdoctor/<did>',editdoctor,name="editdoctor"),
    path('deldoctor/<did>',deldoctor,name="deldoctor"),
    path('editappoint/<aid>',editappoint,name="editappoint"),
    path('delappoint/<aid>',delappoint,name="delappoint"),
    path('editpatient/<pid>',editpatient,name="editpatient"),
    path('delpatient/<pid>',delpatient,name="delpatient"),
    path('viewmsg',viewmsg,name="viewmsg"),
    path('msgdetail/<mid>',msgdetail,name="msgdetail"),
]
