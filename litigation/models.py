from djmoney.models.fields import MoneyField
from django.db import models
from django.urls import reverse
from datetime import date
from core.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from user_management.models import CustomUser


class CaseStatus(TimeStampedModel):
    name = models.CharField(max_length=100)
    value = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(blank=True,null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['value']


class CaseStage(TimeStampedModel):
    name = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class CaseType(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    sender_email = models.EmailField(null=False)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Investor (TimeStampedModel):
    name = models.CharField(max_length=100)
    CaseTypes = models.ManyToManyField(CaseType,blank=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class LawFirm(TimeStampedModel):
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    contact_email = models.EmailField()
    case_types = models.ManyToManyField(CaseType, blank=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Fund (TimeStampedModel):
    name = models.CharField(max_length=100)
    investor = models.ForeignKey(Investor, on_delete=models.PROTECT, null=False)
    allowed_law_firms = models.ManyToManyField(LawFirm,blank=True)
    # Fund parameters

    # Available capital for this fund:
    investment_capital = MoneyField(max_digits=19, decimal_places=4, default_currency='EUR',null=False)
    # Maximum number of claims:
    max_claims_count = models.PositiveIntegerField(default=0,null=False)
    # Maximum sum of all claim amounts:
    max_claims_sum = MoneyField(max_digits=19, decimal_places=4, default_currency='EUR',null=False)
    # Current number of active claims
    current_claims_count = models.PositiveIntegerField(default=0,null=False)
    # Current sum of all claim amounts
    current_claims_sum = MoneyField (max_digits=19, decimal_places=4, default_currency='EUR',default=0,null=True)
    # Currently invested capital
    used_capital = MoneyField (max_digits=19, decimal_places=4, default_currency='EUR',default=0)

    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    @property
    def available_capital(self):
        if (self.used_capital > 0):
            return self.investment_capital - (self.used_capital or Money(amount=0, currency=EUR))
        else:
            return self.investment_capital

    @property
    def remaining_claims_capacity(self):
        return self.max_claims_count - self.current_claims_count

    @property
    def remaining_claims_sum_capacity(self):
        if (self.current_claims_sum.amount > 0):
            return self.max_claims_sum - (self.current_claims_sum or Money(amount=0, currency=EUR))
        else:
            return self.max_claims_sum

    @property
    def claims_sum_utilization_percent(self):
        if (self.max_claims_sum.amount == 0 or self.current_claims_sum.amount == 0):
            return 0
        else:
            return (self.current_claims_sum / self.max_claims_sum) * 100


class Case (TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    law_firm = models.ForeignKey(LawFirm, on_delete=models.PROTECT, null=True)
    case_type = models.ForeignKey(CaseType, on_delete=models.PROTECT,null=True)
    case_status = models.ForeignKey(CaseStatus, on_delete=models.PROTECT,default=1)
    history = HistoricalRecords()

    def __str__(self):
        return self.title


class TaskStatus(models.IntegerChoices):
    OPEN = 0
    IN_PROGRESS = 10
    COMPLETED = 20
    CLOSED = 100

class TaskPriority(models.IntegerChoices):
    LOW = 10
    MEDIUM = 20
    HIGH = 30
    URGENT = 40

class Task(TimeStampedModel):
    #case = models.ForeignKey(Case, on_delete=models.CASCADE)
    title =  models.CharField(max_length=40, blank=False, null=False)
    priority = models.PositiveSmallIntegerField(choices=TaskPriority, default=TaskPriority.MEDIUM, null=True)
    due_date = models.DateField(blank=False, null=True)
    status = models.PositiveSmallIntegerField(choices=TaskStatus, default=TaskStatus.OPEN, null=True)
    description = models.TextField(null=True)
    history = HistoricalRecords()
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,null=True
    )

    class Meta:
        ordering = ["due_date"]

    def get_readable_status(self):
        return TaskStatus(self.status).label

    def get_absolute_url(self):
        return reverse('litigation:task_detail', args=(self.id,))

    @property
    def is_overdue(self):
        return
        #today = date.today()
        #return bool(self.due_back and date.today() > self.due_back)

    def __str__(self):
        return self.title
