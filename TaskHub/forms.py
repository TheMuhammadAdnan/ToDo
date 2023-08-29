from django import forms
from .models import Task,User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'category', 'completed']
        
    
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
        
class LoginForm(AuthenticationForm):
    pass
