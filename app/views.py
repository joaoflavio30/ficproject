from django.shortcuts import render
from .models import Cadete

# Create your views here.
def list_cadete(request):
	cadetes = Cadete.objects.all()
	return render(request, 'index.html', {'cadetes': cadetes})
