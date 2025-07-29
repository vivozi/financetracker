from django.urls import path

from litigation.views import *

def e500_view(request):
    raise Exception("This is a test error")

app_name = 'litigation'
urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path("e500/", e500_view),
]