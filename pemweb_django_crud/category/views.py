from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Category
from . forms import CategoryForm

def category(request):
  form = CategoryForm()
  categories = Category.objects.all()
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid:
      form.save()
    return redirect('/')
  
  context = {'categories': categories, 'CategoryForm':form}
  return render(request, 'category.html', context)