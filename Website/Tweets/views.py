from django.shortcuts import render
# Create your templates here.
from django.http import HttpResponse
from Locations import Locations


def index(request):
    for country in Locations.Locations:
        print(country.full_name)
    return render(request, 'Home/index.html')
