from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:pk>', views.category, name="task-category"),
]
