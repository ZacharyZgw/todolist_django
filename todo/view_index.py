from django.shortcuts import render,HttpResponse
from .models import Todo
def index(request):
    todolist = Todo.objects.all()
    context = {"todolist":todolist}
    return render(request,'index.html',context)