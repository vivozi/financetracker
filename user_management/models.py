from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import TimeStampedModel
from simple_history.models import HistoricalRecords

class CustomUser(AbstractUser,TimeStampedModel):
    # Add any additional fields here
    history = HistoricalRecords()
    notes = models.TextField(blank=True, null=True)

    ADMIN = 1
    KL_STAFF=2
    LAW_FIRM_STAFF=3
    INVESTOR = 4

    ROLE_CHOICES = (
        (ADMIN , "admin"),
        (KL_STAFF , "kl_staff"),
        (LAW_FIRM_STAFF , "law_firm_staff"),
        (INVESTOR , "investor"),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)