from django.shortcuts import render

def homepage(request):
    return render(request,'journal/index.html')

def register(request):
    return render(request,'journal/register.html')

def my_login(request):
    return render(request,'journal/login.html')

def dashboard(request):
    return render(request,'journal/dashboard.html')    
