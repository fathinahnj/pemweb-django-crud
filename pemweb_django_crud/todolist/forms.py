from django import forms  # type: ignore
from django.forms import ModelForm # type: ignore
from . import models
from .models import Task

class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add in a new task'}))

    class Meta:
        model = Task
        fields = ['title', 'category', 'completed']  