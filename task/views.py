from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import FormTask

def task_list(request):
    tasks=Task.objects.all().order_by('-created_at')
    return render(request, 'task_list.html', {
        'tasks':tasks
    })

def add_task(request):
    form=FormTask(request.POST or None)
    title=''
    content=''
    if form.is_valid():
        title=request.POST.get('title')
        content=request.POST.get('content')
        form.save()
        return redirect('tasks')
    return render(request, 'add_task.html', {
        'form':form,
        'title':title,
        'content':content
    })

def update_task(request,id):
    task=get_object_or_404(Task,id=id)
    form=FormTask(request.POST or None, instance=task)
    if form.is_valid():
         form.save()
         return redirect('tasks')
    return render(request, 'update_task.html', {
        'form':form,
        'title':task.title,
        'content':task.content
    })

def delete_task(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=='POST':
        task.delete()
        return redirect('tasks')
    return render(request, 'delete_task.html',{
        'task':task
    })