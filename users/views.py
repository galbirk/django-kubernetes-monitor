from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from monitor.models import Users
from passlib.hash import pbkdf2_sha256

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            if form.cleaned_data.get('cluster') != '':
                cluster = form.cleaned_data.get('cluster')
                user = User.objects.filter(username=user_name).first()
                users = Users(name=user,cluster=cluster)
                users.save()
            else:
                user = User.objects.filter(username=user_name).first()
                users = Users(name=user,cluster='None')
                users.save()
            messages.success(request,'Your Account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{ 'form' : form })