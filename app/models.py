from django.db import models

# Create your models here.
from django.db import models

class Cadete(models.Model):
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

