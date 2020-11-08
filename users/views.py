from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from users.models import User_Role

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_name = form.cleaned_data.get('username')
            role = form.cleaned_data.get('role')
            user = User.objects.filter(username=user_name).first()
            user_role = User_Role(user=user,role=role)
            user_role.save()
            messages.success(request,'Your Account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{ 'form' : form })