from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def showscore(request):
    score = Score.objects.all()
    context= {'score':score}
    return render(request,'showscore.html',context)

def register(request):
    if request.method=='POST':
        data = request.POST.copy()
        user_name = data.get('user-name')
        email = data.get('email')
        password = data.get('password')
        repassword = data.get('repassword')
        if user_name=="" or user_name.strip()=="":
            messages.info(request,"Please enter username")
            return redirect('register') 
        if email=="" or email.strip()=="":
            messages.info(request,"Please enter email")
            return redirect('register') 
        if password=="" or password.strip()=="":
            messages.info(request,"Please enter password")
            return redirect('register') 
        if password==repassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')    
            else:
                newuser=User()
                newuser.username=user_name
                newuser.email=email
                newuser.set_password(password)
                newuser.save()
        else:
            messages.info(request,"Password mismatch")
            return redirect('register')
        return redirect('home')
    return render(request,'register.html')