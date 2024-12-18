from django import forms 
from django.forms import ModelForm
from . import models
from .models import Category

class CategoryForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add in a new category'}))

    class Meta:
        model = Category
        fields = "__all__"