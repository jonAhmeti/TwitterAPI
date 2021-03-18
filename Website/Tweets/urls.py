from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cities', views.cities, name='cities'),
    path('search', views.search_tweets, name='search'),
]
