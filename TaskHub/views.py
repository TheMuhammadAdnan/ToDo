from django.shortcuts import render, redirect
from .models import Task,TaskCategory,User
from .forms import TaskForm

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
        else:
            print(form.errors)
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form':form})

def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks':tasks})        
