from django import forms 
from django.forms import ModelForm
from . import models
from .models import Task

  # fields = ['title', 'completed', 'due_date']
  # widgets = {
  #           'title': forms.TextInput(attrs={
  #               'class': 'form-control',
  #               'placeholder': 'Add in a new task'
  #           }),
  #           'completed' : forms.BooleanField(attrs={
  #             'class' : 'form-control'
  #           })
  #           ,
  #           'due_date': forms.DateTimeInput(attrs={
  #               'class': 'form-control',
  #               'type': 'datetime-local'
  #           }),
  #       }
class TaskForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add in a new task'}))

    class Meta:
        model = Task
        fields = "__all__"