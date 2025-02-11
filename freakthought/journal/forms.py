from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.forms.widgets import TextInput,PasswordInput
from django.forms import ModelForm
from .models import Thought

class ThoughtForm(ModelForm):
    class Meta:
        model = Thought
        fields = '__all__'  

        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class LoginForm(AuthenticationForm):  

    username = forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

