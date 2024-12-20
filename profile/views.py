from django.shortcuts import render
from .models import Cadete
from django.http import JsonResponse
from app.utils import fetch_api_data

# Create your views here.
def list_cadete(request):
	cadetes = Cadete.objects.all()
	return render(request, 'index.html', {'cadetes': cadetes})


def my_view(request):
    try:
        data = fetch_api_data()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

