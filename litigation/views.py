from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from .forms import TaskForm
from .models import Task


# Create your views here.
class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'

class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = 'task_detail'

class TaskDetailView(generic.CreateView):
    model = Task
    context_object_name = 'task_create'
    fields = ["title","description","priority","due_date","status"]

    def get_success_url(self):
        return reverse("tasks")

class TaskDetailView(generic.UpdateView):
    model = Task
    context_object_name = 'task_update'
    form_class = TaskForm
    #fields = ["title", "description", "priority", "due_date", "status"]

    def get_success_url(self):
        return reverse("litigation:tasks")