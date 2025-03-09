from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from . models import Task

#Adding task function

def addTask(request):
    task = request.POST["task"]
    Task.objects.create(task = task)
    return redirect("home")

#marks as done function

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("home")

#Undone function creation

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect("home")

#Edit task function

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_task = request.POST["task"]
        get_task.task = new_task
        get_task.save()
        return redirect("home")
    else:
        context = {
            "get_task" : get_task,
        }
        return render(request, "edit_task.html", context)

#Delete task function
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("home")