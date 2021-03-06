from django.shortcuts import render
from django.utils import timezone
from Todo_App.models import Todo
from django.http import HttpResponseRedirect


def home(request):
    todo_item = Todo.objects.all().order_by("-added_date")
    return render(request, 'TodoApp/index.html', {
        'todo_item': todo_item
    })


def add_todo(request):
    # print(request.POST)
    current_date = timezone.now()
    content = request.POST['text']
    Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
