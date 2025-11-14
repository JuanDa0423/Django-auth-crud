from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#modelo de tarea
class Task(models.Model):
    Title = models.CharField(max_length=200)
    description= models.TextField(blank=True)
    created= models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    impotant= models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Title +"- by-" + self.user.username