from django.shortcuts import render
from django import http
from django.views import generic
from . import models
from .Locations import Locations
from .ISO639Lang import LangISO
from .API.API import SearchTweets
import json
import datetime


def saveToDb(tweets):
    for tweet in tweets:
        obj_tweet = models.Tweet()
        obj_user = models.User()
        for (key, value) in tweet.items():
            if key == 'id_str':
                obj_tweet.id_str = value
            elif key == 'full_text':
                obj_tweet.text = value
            elif key == 'hashtags':
                for hashtag in value:
                    obj_tweet.hashtags = ''
                    for (key, value) in hashtag.items():
                        if key == 'text':
                            obj_tweet.hashtags += f'{value},'
            elif key == 'source':
                obj_tweet.source = value
            elif key == 'user':
                for (key, value) in value.items():
                    if key == 'id_str':
                        obj_tweet.user_id = value
                        obj_user.id_str = value
                    elif key == 'name':
                        obj_user.name = value
                    elif key == 'screen_name':
                        obj_user.screen_name = value
                    elif key == 'location':
                        obj_user.location = value
                    elif key == 'description':
                        obj_user.description = value
                    elif key == 'followers_count':
                        obj_user.followers_count = value
                    elif key == 'friends_count':
                        obj_user.friends_count = value
                    elif key == 'created_at':
                        obj_user.created_at = value
                    elif key == 'verified':
                        obj_user.verified = value
            elif key == 'geo':
                obj_tweet.geo = 'None'
            elif key == 'place':
                if value is not None:
                    obj_tweet.place = ''
                    for (key, value) in value.items():
                        if key == 'full_name':
                            obj_tweet.place += f'full_name={value};'
                        elif key == 'country':
                            obj_tweet.place += f'country={value};'
            elif key == 'possibly_sensitive':
                obj_tweet.possibly_sensitive = value
            elif key == 'lang':
                obj_tweet.lang = value
            elif key == 'created_at':
                obj_tweet.created_at = value
        try:
            userDB = models.User.objects.get(id_str=obj_user.id_str)
        except models.User.DoesNotExist:
            obj_user.save()
        try:
            tweetDB = models.Tweet.objects.get(id_str=obj_tweet.id_str)
            print(f'Tweet object already exists in database: {tweetDB}')
        except models.Tweet.DoesNotExist:
            obj_tweet.save()
    print(f'Users: {models.User.objects.all()}')
    print(f'Tweets: {models.Tweet.objects.all()}')


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
    languages.sort(key=lambda x: x[1])

    return render(request, 'Home/index.html', {'context_countries': countries, 'context_lang': languages})


def search_tweets(request):
    params = {}
    if request.method == 'POST':
        params.update({'tweet_mode': 'extended'})
        for (key, value) in request.POST.items():
            if key == 'count' and value == '':
                params.update({key: 1})
            elif key == 'csrfmiddlewaretoken' or key == 'byPlace' or value == '':
                continue
            else:
                params.update({key: value})

    if 'radius' in params and 'geocode' in params:
        params.update({'geocode': f"{params.get('geocode')},{params.get('radius')}km"})
        params.pop('radius')
        params.pop('country')
    elif 'radius' in params and 'geocode' not in params:
        params.pop('radius')

    if 'q' not in params:
        return http.HttpResponseRedirect('.')

    req = SearchTweets()
    req.set_params(**params)

    response = req.send()
    jsonResponse = json.loads(response.content)
    tweets = jsonResponse['statuses']
    saveToDb(tweets)
    return render(request, 'Tweets/tweet_list.html', {'context_tweets': tweets})


def cities(request):
    cityArray = []
    for country in Locations:
        if country.name == request.GET['country']:
            for var in country.value:
                if var.name != 'full_name':
                    cityArray.append(var.value)

    cityArray.sort(key=lambda index: index[1])
    return http.JsonResponse(cityArray, safe=False)
