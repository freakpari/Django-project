from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def homepage(request):
    return render(request, 'journal/index.html')

def register(request):
    form = CreateUserForm()  # Initialize an empty form

    if request.method == 'POST':
        form = CreateUserForm(request.POST)  # Populate the form with POST data

        if form.is_valid():  # This should be inside the POST check
            form.save()
            return redirect('my-login')  # Redirect to login after successful registration

    context = {'RegisterationForm': form}
    return render(request, 'journal/register.html', context)

def my_login(request):
    form = LoginForm()  # Initialize an empty form correctly with parentheses

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Populate form with POST data

        if form.is_valid():  # Check if the form is valid **inside the POST check**
            username = form.cleaned_data.get('username')  # Use cleaned_data instead of request.POST
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:  # Ensure this check is **inside** the form validation block
                login(request, user)  # Use login from django.contrib.auth
                return redirect('dashboard')  # Redirect to dashboard on success
            else:
                messages.error(request, "Invalid username or password")  # Show error message if authentication fails

    context = {'LoginForm': form}
    return render(request, 'journal/login.html', context)

def dashboard(request):
    return render(request, 'journal/dashboard.html')
