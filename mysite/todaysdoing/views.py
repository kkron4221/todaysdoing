from django.shortcuts import render
from .models import TODO

def index(request):
    return (request, 'todaysdoing/doinglist.html')