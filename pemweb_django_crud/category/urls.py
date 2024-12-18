from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_category, name="task-category"),  
    path('update-category/<int:pk>/', views.updateCategory, name="update-category"),  
    path('delete-category/<int:pk>/', views.deleteCategory, name="delete-category"),  
    path('category-dropdown/', views.category_dropdown, name='category-dropdown'),  
]