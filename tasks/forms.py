from django.forms import ModelForm
from .models import Task
from django import forms
#modelo de formulario de tarea
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['Title', 'description', 'impotant'] 
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Write a title'}),
            'description' : forms.Textarea(attrs ={'class':'form-control', 'placeholder': 'Describe your task'}),
            'impotant' : forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }