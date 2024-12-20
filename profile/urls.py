from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('', views.list_cadete, name='list_cadete'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='cadet_profile'),
]
