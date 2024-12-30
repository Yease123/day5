from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.shortcuts import render,redirect
# Create your views here.

def hello(request):
    return HttpResponse("Welcome to internship program")
def task_list(request):
    task=Task.objects.all()
    return render(request,'tasks/task_list.html',{"task":task})
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})
