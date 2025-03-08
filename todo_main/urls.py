from django.contrib import admin
from django.urls import path, include
from todo_main import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name = "home"),
    path("todo/", include("todo.urls")), 
    
    
]
