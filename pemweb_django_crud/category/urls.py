from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_category, name="task-category"),
    path('update-category/<str:pk>', views.updateCategory, name="update-category"),
    # path('delete-category/<str:pk>', views.deleteCategory, name="delete-category")
]
