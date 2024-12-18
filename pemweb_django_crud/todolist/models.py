from django.db import models
from category.models import Category
# class Category(models.Model):
#   title = models.CharField(max_length=30)
  
#   def _str_(self):
#     return self.title 

class Task(models.Model):
  title = models.CharField(max_length=300)
  completed = models.BooleanField(default=False)
  # due_date = models.DateTimeField(null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True) 
  
  # def _str_(self):
  #   return self.id