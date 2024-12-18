from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Category
from . forms import CategoryForm

def create_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid:
      form.save()
    return redirect('/')
  else:
    form = CategoryForm()
    
  categories = Category.objects.all()
  context = {'categories': categories, 'form':form}
  return render(request, 'category.html', context)