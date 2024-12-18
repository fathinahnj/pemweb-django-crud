from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse  # type: ignore
from .models import Task, Category
from .forms import TaskForm

def index(request):
    form = TaskForm() 
    tasks = Task.objects.all()
    categories = Category.objects.all()  # Fetch all categories

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-list')  # Redirect to 'todo-list' using its name

    context = {'tasks': tasks, 'TaskForm': form, 'categories': categories}
    return render(request, 'todo.html', context)

def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    categories = Category.objects.all()  # Fetch categories if needed in the template

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo-list')  # Redirect to homepage after saving
    else:
        form = TaskForm(instance=task)

    context = {'form': form, 'task': task, 'categories': categories}
    return render(request, 'update-task.html', context)


def deleteTask(request, pk):
  task = Task.objects.get(id=pk)
  if request.method == 'POST':
    task.delete()
    return redirect('/')
  context = {'task': task}
  return render(request, 'delete-task.html', context)
  