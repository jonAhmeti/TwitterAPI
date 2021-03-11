from django.shortcuts import render
import Locations

# Create your templates here.
from django.http import HttpResponse


def index(request):
    for x in Locations:
        print(x)
    return render(request, 'Home/index.html')
