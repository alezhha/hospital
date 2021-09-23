from django.shortcuts import render
from .models import Hospital

# Create your views here.

def index(request):
    return render(request, 'index.html', {"hospitals":Hospital.objects.all()})