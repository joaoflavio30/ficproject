from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
"""class Cadete(models.Model):
    id_cadete = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    current_project = models.CharField(max_length=100, blank=True, null=True)
    recommended_project = models.CharField(max_length=100, blank=True, null=True)
    past_projects = models.JSONField(blank=True, null=True)
    black_hole = models.FloatField(default=0.0)
    hours = models.PositiveIntegerField(default=0)
    means_of_contact = models.JSONField(blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.login
"""

def get_first_rank_days():
    return (timezone.now() + datetime.timedelta(days=30)).date()

class CadetProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cadet_profile')
    hours = models.PositiveIntegerField(default=0)
    current_project = models.CharField(max_length=100, null=True)
    past_projects = models.JSONField(null=True)
    black_hole_day = models.DateField(default=get_first_rank_days)
    means_of_contact = models.JSONField()

    def __str__(self):
        return self.user.username
