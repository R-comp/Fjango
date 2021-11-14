from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

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
        newuser=User()
        newuser.username=user_name
        newuser.email=email
        newuser.set_password(password)
        newuser.save()   
        return redirect('home')
    return render(request,'register.html')