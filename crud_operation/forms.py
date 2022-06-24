from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from .models import Post



class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username':'username','first_name':'First Name','last_name':'Last Name',
        'email':'Email Address'}



class LoginForm(AuthenticationForm):
    fields = ['username','password']
    labels = {'username':'Username','password': 'Password'}

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}