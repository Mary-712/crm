from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def log(request):
    return redirect('dashboard')

def new(request):
    return render(request,'new.html')

def dashboard(request):
    return render(request,'dashboard.html')
def archieve(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request, 'Archieve.html', {'item_ids': item_ids})