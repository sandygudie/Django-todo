from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.createTodo, name='addtodo_url'),
    path('update/<int:todoId>', views.updateTodo, name= 'update_url'),
    path('delete/<int:todoId>', views.deleteTodo, name= 'delete_url'),
]