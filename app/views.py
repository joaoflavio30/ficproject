from django.shortcuts import render
from django.http import HttpResponse
from .models import Cadete

# Create your views here.
def list_cadete(request):
	cadetes = Cadete.objects.all()
	return render(request, 'index.html', {'cadetes': cadetes})

def index(request):
	return render(request, 'app/index.html')