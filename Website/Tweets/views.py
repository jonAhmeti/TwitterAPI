from django.shortcuts import render

# Create your templates here.
from django.http import HttpResponse


def index(request):

    return render(request, 'Home/index.html')
