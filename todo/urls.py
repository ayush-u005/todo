from django.urls import path
from . import views

urlpatterns = [
    #Add task
    path("add/", views.addTask, name = "addTask"),
    #Marking as done
    path("mark_as_done/<int:pk>/", views.mark_as_done, name = "mark_as_done"),
    #Marking as undone
    path("mark_as_undone/<int:pk>/", views.mark_as_undone, name = "mark_as_undone"),
    #Editing the task
    path("edit_task/<int:pk>/", views.edit_task, name = "edit_task"),
    #Delete task
    path("delete_task/<int:pk>/", views.delete_task, name = "delete_task"),


]
