from django.shortcuts import render
from django.http import JsonResponse
from profile.utils import fetch_api_data
from .models import CadetProfile
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
def list_cadete(request):
    errors = ''
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        if (not name):
            return render(request, 'index.html', {'errors': ['you must put a valid username']})
        if (not password):
            return render(request, 'index.html', {'errors': ['you must put a valid password']})
        new_user = User.objects.create(username=name, password=password)
        new_user.save()
        new_user.refresh_from_db()
        new_user_profile = CadetProfile.objects.create(user=new_user, means_of_contact={'telephone': "40028922"})
        new_user_profile.save()
        return HttpResponse("user created successfully")

    return render(request, 'index.html')


def my_view(request):
    try:
        data = fetch_api_data()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

