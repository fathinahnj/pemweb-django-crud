from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='todo-list'),
    path('update-task/<str:pk>', views.updateTask, name="update-task"),
    path('delete-task/<str:pk>', views.deleteTask, name="delete-task"),
    path('update-category/<int:pk>/', views.TaskForm, name='update-category'),
]
