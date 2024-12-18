from django.db import models # type: ignore

class Category(models.Model):
  title = models.CharField(max_length=30)
  
  # class Meta:
  #       db_table = 'todolist_category'
  
  def __str__(self):
    return self.title 
  