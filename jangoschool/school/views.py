from django.shortcuts import render
from .models import *
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
    return render(request,'register.html')