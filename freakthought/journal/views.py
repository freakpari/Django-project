from django.shortcuts import render,redirect
from . forms import CreateUserForm

def homepage(request):
    return render(request,'journal/index.html')

def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('my-login')
    
    context ={'RegisterationForm' : form}
    return render(request,'journal/register.html',context)

def my_login(request):
    return render(request,'journal/login.html')

def dashboard(request):
    return render(request,'journal/dashboard.html')    
