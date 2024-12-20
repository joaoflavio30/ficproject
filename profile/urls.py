from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('', views.list_cadete, name='list_cadete'),
]
