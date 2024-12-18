from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Category
from . forms import CategoryForm

def create_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid:
      form.save()
    return redirect('/category')
  else:
    form = CategoryForm()
    
  categories = Category.objects.all()
  context = {'categories': categories, 'form':form}
  return render(request, 'category.html', context)

def updateCategory(request, pk):
  category = Category.objects.get(id=pk)
  form = CategoryForm(instance=category)
  if request.method == 'POST':
    form = CategoryForm(request.POST, instance=category)
    if form.is_valid:
      form.save()
    return redirect('/category')
  context = {'form':form}
  return render(request, 'update-category.html', context)

def deleteCategory(request, pk):
  category = Category.objects.get(id=pk)
  if request.method == 'POST':
    category.delete()
    return redirect('/category')
  context = {'category': category}
  return render(request, 'delete-task.html', context)