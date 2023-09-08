from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

   
urlpatterns = [
    path('createtask/', views.create_task, name='create_task'),
    path('tasklist/', views.task_list, name='task_list'),
    path('signup/', views.signup, name='signup'),  # Use your custom signup view
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.homepage, name='home' ),
    path('update_task/<int:task_id>/',views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
]