from django.urls import path
from core.views import AboutView
import core.views

def e500_view(request):
    raise Exception("This is a test error")

app_name = 'core'
urlpatterns = [
    #path("", AboutView.as_view()),
    path('',core.views.dashboard,name='dashboard'),
    path("e500/", e500_view),
]