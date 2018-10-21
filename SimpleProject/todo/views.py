from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import TodoSerializer, UserRegSerializer
from django.views.decorators.http import require_POST


def index(request):
'''
    Method that handles the UI, Form and Displays the Todo Tasks.
'''
    todo = Todo.objects.all()
    form = TodoForm()

    args = {
        'todo_lst':todo,
        'form':form,
    }
    return render(request,'index.html', args)

def complete(request, todo_id):

    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('/')

@require_POST
def add(request):

    form = TodoForm(request.POST or None)

    if form.is_valid():
        todo = Todo(text=request.POST['text'])
        todo.save()
    return redirect('/')

def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('/')

def del_all(request):
    Todo.objects.all().delete()

    return redirect('/')


class TodoViewSets(viewsets.ModelViewSet):
'''
    Class that handles all the Api request related to Todo Model.
'''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
