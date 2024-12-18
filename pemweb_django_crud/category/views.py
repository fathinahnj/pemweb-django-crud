from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.http import HttpResponse  # type: ignore
from .models import Category
from .forms import CategoryForm

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-category')  
    else:
        form = CategoryForm()

    categories = Category.objects.all()
    context = {'categories': categories, 'form': form}
    return render(request, 'category.html', context)


def updateCategory(request, pk):
    category = get_object_or_404(Category, id=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('task-category')
    else:
        form = CategoryForm(instance=category)

    context = {'form': form, 'category': category}
    return render(request, 'update-category.html', context)

def deleteCategory(request, pk):
    category = get_object_or_404(Category, id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('task-category') 
    context = {'category': category}
    return render(request, 'delete-category.html', context)

def category_dropdown(request):
    categories = Category.objects.all()
    return render(request, 'category_dropdown.html', {'categories': categories})