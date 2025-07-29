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

class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'litigation/task_create.html'
    context_object_name = 'task_create'

    def get_success_url(self):
        return reverse("litigation:tasks")

class TaskUpdateView(generic.UpdateView):
    model = Task
    context_object_name = 'task_update'
    form_class = TaskForm
    template_name = 'litigation/task_form.html'

    def get_success_url(self):
        return reverse("litigation:tasks")