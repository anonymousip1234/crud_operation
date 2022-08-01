"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from crud_operation import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('mainsignup/',views.mainsignup,name='mainsignup'),
    path('producersignup/',views.producersignup,name='producersignup'),
    path('reportersignup/',views.reportersignup,name='reportersignup'),
    path('viewersignup/',views.viewersignup,name='viewersignup'),
    path('login/',views.login,name = 'login'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('admindashboard/',views.admindashboard,name = 'admindashboard'),
    path('addpost/',views.addpost,name='addpost'),
    path('editpost/<id>',views.editpost,name='editpost'),
    path('deletpost/<id>',views.deletepost,name='deletepost'),
    path('logout/',views.logout,name = 'logout')
    

]
