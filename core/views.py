from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.views.generic import TemplateView

from user_management.models import CustomUser as User
from litigation.models import Case,LawFirm, CaseStatus

class AboutView(TemplateView):
    template_name = "core/about.html"

@login_required
def dashboard (request):
    context = {
        'stats': {
            'total_users': User.objects.count(),
            'total_cases': Case.objects.count(),
            'total_law_firms': LawFirm.objects.count(),
            #'pending_cases': Case.query.filter_by(status=CaseStatus.PENDING).count()
        }
    }
    return render(request,"core/dashboard.html",
                  context=context)

def error_404(request, exception):
    return render(request, 'error_404.html', status=404)

def error_500(request):
    return render(request, 'error_500.html', status=500)