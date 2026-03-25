from django.shortcuts import get_object_or_404, redirect, render
from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all().order_by("-created_at")
    form = TodoForm()

    return render(request, "todos/todo_list.html", {
        "todos": todos,
        "form": form,
    })


def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("todo_list")


def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todo_list")


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("todo_list")