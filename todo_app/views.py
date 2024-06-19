from django.shortcuts import render, redirect
from todo_app.models import Todo
from .forms import TodoForm


def createTodo(request):
    form = TodoForm(auto_id=True)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "addTodo.html", context)


def index(request):
    data = Todo.objects.all().values()
    context = {
        "todolist": data,
    }
    return render(request, "index.html", context)


def updateTodo(request, todoId):
    obj = Todo.objects.get(id=todoId)

    form = TodoForm(auto_id=True, instance=obj)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "addTodo.html", context)


def deleteTodo(request, todoId):
    obj = Todo.objects.get(id=todoId)

    if request.method == "POST":
        obj.delete()
        return redirect("index")
    context = {
        " obj": obj,
    }
    return render(request, "confirmdelete.html", context)
