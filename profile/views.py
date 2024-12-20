from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from profile.utils import fetch_api_data
from .models import CadetProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def list_cadete(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        if (not name):
            return render(request, 'index.html', {'errors': ['you must put a valid username']})
        if (not password):
            return render(request, 'index.html', {'errors': ['you must put a valid password']})
        new_user = User.objects.create(username=name)
        new_user.set_password(password)
        new_user.save()
        new_user_profile = CadetProfile.objects.create(user=new_user, means_of_contact={'telephone': "40028922"})
        new_user_profile.save()
        return HttpResponse("user created successfully")

    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    try:
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect(reverse('profile:cadet_profile'))
    except Exception as e:
        print("INVALID USER")
        return redirect(reverse('profile:login'))
    return redirect(reverse('profile:login'))

@login_required(login_url=reverse_lazy('profile:login'))
def profile(request):
    return HttpResponse("hello world")


def my_view(request):
    try:
        data = fetch_api_data()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

