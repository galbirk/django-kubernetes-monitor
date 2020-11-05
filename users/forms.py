from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    cluster = forms.CharField(label='Cluster Name', required=False)
    
    class Meta:
       model = User
       fields = ['username','cluster', 'password1', 'password2'] 

# class LoginForm(forms.Form):
#     class Meta:
#        model = User
#        fields = ['username','password'] 
