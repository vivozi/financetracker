from django.contrib import admin
from allauth.account.decorators import secure_admin_login

from django.contrib.admin import ModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import Task,LawFirm,Investor,Fund,Case,CaseType,CaseStatus
# Register your models here.

#admin.site.register(CaseType)
admin.site.register(Task)
admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

@admin.register(CaseType)
class CaseTypeAdmin(SimpleHistoryAdmin, ModelAdmin):
    pass

@admin.register(CaseStatus)
class CaseStatusAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('name', 'value')

@admin.register(Fund)
class FundAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('name','investor','investment_capital','max_claims_count')

@admin.register(LawFirm)
class LawFirmAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('name', 'address', 'contact_email')

@admin.register(Case)
class CaseAdmin(SimpleHistoryAdmin, ModelAdmin):
    pass

@admin.register(Investor)
class InvestorAdmin(SimpleHistoryAdmin, ModelAdmin):
    pass