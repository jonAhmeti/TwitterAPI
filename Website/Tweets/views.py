from django.shortcuts import render
from django.http import JsonResponse
from .Locations import Locations
from .ISO639Lang import LangISO


def index(request):
    countries = []
    for x in Locations:
        for y in x.value:
            if y.name == 'full_name':
                countries.append((y.value, x.name))
    countries.sort()

    languages = []
    for lang in LangISO:
        language_names = lang.value[1].split(',')
        if len(language_names) > 1:
            languages.append((lang.value[0], language_names[0]))
        else:
            languages.append(lang.value)
    languages.sort(key=lambda x:x[1])

    return render(request, 'Home/index.html', {'context_countries': countries, 'context_lang': languages})


def cities(request):
    cityArray = []
    for country in Locations:
        if country.name == request.GET['country']:
            for var in country.value:
                if var.name != 'full_name':
                    cityArray.append(var.value)

    cityArray.sort(key=lambda index: index[1])
    return JsonResponse(cityArray, safe=False)
