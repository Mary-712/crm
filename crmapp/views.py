from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def log(request):
    return redirect('home')

def new(request):
    return render(request,'new.html')