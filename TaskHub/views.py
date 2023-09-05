from django.shortcuts import render, redirect
from .models import Task,TaskCategory,User
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


def homepage(request):
    return render(request, 'base.html')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # Associate the task with the logged-in user
            task.save()
            return redirect('task_list')
        else:
            print(form.errors)
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form':form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks':tasks})        


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form':form, 'task':task})