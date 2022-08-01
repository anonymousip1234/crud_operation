from boto import UserAgent
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from psutil import users
from .forms import signupform,LoginForm,Postform
from django.contrib.auth import authenticate,login as auth_login, logout as django_logout
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.

#Home Page
def home(request):
    return render(request,'home.html')



#Main signup Page
def mainsignup(request):
    return render(request,'mainsignup.html')

#All 3 types of signup page

def reportersignup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user =form.save()

            group = Group.objects.get(name='reporter')
            user.groups.add(group)
    else:
        form = signupform()
    form = signupform()

    return render(request,'reportersignup.html',{'form':form})

def producersignup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user =form.save()

            group = Group.objects.get(name='producer')
            user.groups.add(group)
    else:
        form = signupform()
    form = signupform()
    return render(request,'producersignup.html',{'form':form})

def viewersignup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            user =form.save()

            group = Group.objects.get(name='viewer')
            user.groups.add(group)
    else:
        form = signupform()
    form = signupform()
    return render(request,'viewersignup.html',{'form':form})



#login page
def login(request):
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request = request,data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname,password = upass)
                if user is not None:
                    auth_login(request,user)
                    gps = request.user.groups.all()
                    for i in gps:
                        if str(i) == 'admin':

                            return HttpResponseRedirect('/admindashboard/')
                        else:
                            return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()

            return render(request,'login.html',{'form':form })
    else:
        return HttpResponseRedirect('/dashboard/')
#dashboard page
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        gps = user.groups.all()

        for i in gps:
            a = str(i)
        return render(request,'dashboard.html',  {'posts':posts,'groups':gps,'a':a} )

def admindashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        gps = user.groups.all()
        return render(request,'admindashboard.html',  {'posts':posts,'groups':gps,} )


    

#add edit and delete options
def addpost(request):
    
    if request.method == 'POST':
        
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            last_id= Post.objects.last().id
            t = Post.objects.get(id=last_id)
            t.updated_by = str(request.user.groups.all()[0])
            t.save()
            
            form = Postform()
    else:

        form = Postform()
    return render(request,'addpost.html',{'form':form})


def editpost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = Postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                
        else:

            pi = Post.objects.get(pk=id)
            form = Postform(instance=pi)
        return render(request,'editpost.html',{'form':form})

def deletepost(request,id):
    if request.method =='POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/admindashboard/')

#logout page
def logout(request):
   
    django_logout(request)

    return HttpResponseRedirect('/')