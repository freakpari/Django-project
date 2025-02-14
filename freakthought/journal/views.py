from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm , ThoughtForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from .models import Thought


def homepage(request):
    return render(request, 'journal/index.html')

def register(request):
    form = CreateUserForm() 

    if request.method == 'POST':
        form = CreateUserForm(request.POST)  
        if form.is_valid():  
            form.save()
            messages.success(request,"user created successfully!")
            return redirect('my-login')  

    context = {'RegisterationForm': form}

    return render(request, 'journal/register.html', context)

def my_login(request):
    form = LoginForm()  

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  
        if form.is_valid(): 
            
            username = form.cleaned_data.get('username')  
            
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:  
                login(request, user)  
                return redirect('dashboard') 
            else:
                messages.error(request, "Invalid username or password")  

    context = {'LoginForm': form}
    return render(request, 'journal/login.html', context)


def user_logout(request):
    
    auth.logout(request)
    
    return redirect("")
@login_required(login_url = 'my-login' )
def dashboard(request):
    return render(request, 'journal/dashboard.html')

@login_required(login_url = 'my-login' )
def create_thought(request):
    
    form = ThoughtForm()
    if request.method == 'POST':
            form = ThoughtForm(request.POST)  
    if form.is_valid():  
            thought = form.save(commit=False)
            
            thought.user = request.user
            
            thought.save()
            
            return redirect('my-thoughts')
    context = {'CreateThoughtForm': form}
    
    return render(request, 'journal/create-thought.html', context)


@login_required(login_url = 'my-login' )
def my_thoughts(request):
    current_user = request.user.id
    
    thought = Thought.objects.all().filter(user=current_user)
    
    context = {'AllThoughts': thought}
    
    return render(request, 'journal/my-thoughts.html',context)


@login_required(login_url = 'my-login' )
def update_thought(request, pk):
    
    thought = Thought.objects.get(id=pk)
    
    form = ThoughtForm(instance=thought)
    
    if request.method == 'POST':
        form = ThoughtForm(request.POST,instance=thought)  
        
    if form.is_valid():
        form.save() 
        
        return redirect('my-thoughts')   
    context= { 'UpdateThought' : form}
    return render(request, 'journal/update-thought.html',context)

