from django.urls import path

from .views import todo_list, todo_detail, todo_create

urlpatterns = [
    path("todos/", todo_list, name="todo_list"),
    path("todos/<int:id>", todo_detail, name="todo_detail"),
    path("create-todo/", todo_create, name="create_todo")
]
