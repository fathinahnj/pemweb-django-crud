from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
  tasks = Task.objects.all()
  context = {'tasks': tasks}
  return render(request, 'todo.html', context)