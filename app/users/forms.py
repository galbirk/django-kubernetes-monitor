from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    #role = forms.CharField(label='Role Name', required=True)
    role = forms.ChoiceField(choices=(
        ('partner','partner'),
        ('client','client')
         ),required=True)
    
    class Meta:
       model = User
       fields = ['username','role', 'password1', 'password2']  
