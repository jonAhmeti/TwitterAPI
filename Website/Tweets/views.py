from django.shortcuts import render
from django.http import JsonResponse
from .Locations import Locations


def index(request):
    countries = []
    for x in Locations:
        for y in x.value:
            if y.name == 'full_name':
                countries.append((y.value, x.name))

    countries.sort()

    return render(request, 'Home/index.html', {'context_countries': countries})


def cities(request):
    cityArray = []
    for country in Locations:
        if country.name == request.GET['country']:
            for var in country.value:
                if var.name != 'full_name':
                    cityArray.append(var.value)

    cityArray.sort(key=lambda index: index[1])
    return JsonResponse(cityArray, safe=False)
