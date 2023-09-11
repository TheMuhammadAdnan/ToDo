from django.shortcuts import render, redirect, get_object_or_404 
from .models import Task,TaskCategory,User
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from .forms import TaskSearchForm



def homepage(request):
    return render(request, 'base.html') # for what purpose we have this view?

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # Associate the task with the logged-in user
            task.save()
            return redirect('task_list')
        else:
            print(form.errors) ## instead of print the error on console display the form related errors on FE
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form':form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    # Handle the search query if provided
    search_form = TaskSearchForm(request.GET)
    if search_form.is_valid():  # handle the case if form is not valid
        search_query = search_form.cleaned_data['search_query']
        tasks = tasks.filter(title__icontains=search_query) # make the search more dynamic user can also search based on the content or description in the task?
    return render(request, 'task_list.html', {'tasks': tasks, 'search_form': search_form})        


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # handle the case if form is not valid
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) # code is not secured the task can be updated the not belongs to the same user, add a check that task is belongs to the same user that send request to update the task
    
    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():  # handle the case if form is not valid
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form':form, 'task':task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) # code is not secured the task can be deleted the not belongs to the same user, add a check that task is belongs to the same user that send request to delete the task
    
    if request.method=="POST":
        task.delete()
        return redirect('task_list')
    else:
        return render(request, 'delete_task.html', {'task':task})
    

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # handle the case if form is not valid
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect(reverse_lazy('login'))  # Redirect to the login page using reverse_lazy
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): # handle the case if form is not valid
            login(request, form.get_user())
            return redirect('task_list')  # Redirect to the task list page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})