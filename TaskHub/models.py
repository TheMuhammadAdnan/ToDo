from django.db import models
from django.contrib.auth.models import User

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    category = models.ForeignKey('TaskCategory', on_delete=models.SET_NULL, null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title    
    
