from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo_app/todo_list.html", context)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo_app/todo_detail.html", context)

def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
        # print(form.cleaned_data)
        # name = form.cleaned_data['name']
        # description = form.cleaned_data['description']
        # due_date = form.cleaned_data['due_date']
        # print(name, description, due_date)

        # new_todo = Todo.objects.create(name=name, description=description, due_date=due_date)
        # create todo object
        pass
    context = {
        "form": form
    }
    return render(request, "todo_app/todo_create.html", context)

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        "form": form
    }
    return render(request, "todo_app/todo_update.html", context)

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')