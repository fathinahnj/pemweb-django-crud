from django import forms 
from django.forms import ModelForm
from . import models
from .models import Task

class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add in a new task'}))

    class Meta:
        model = Task
        fields = ['title', 'category', 'completed']  