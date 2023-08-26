from . import views
from django.urls import path

urlpatterns = [
    path('createtask/', views.create_task, name='create_task'),
    path('tasklist/', views.task_list, name='task_list'),
    
]