from django.db import models # type: ignore

class Category(models.Model):
  title = models.CharField(max_length=30)
  
  def __str__(self):
    return self.title 

class Task(models.Model):
  title = models.CharField(max_length=300)
  completed = models.BooleanField(default=False)
  # due_date = models.DateTimeField(null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks", default=1, null=True, blank=True) 
  
  def __str__(self):
    return self.title 
  