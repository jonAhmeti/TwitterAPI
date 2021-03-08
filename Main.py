import os
import Credentials
import requests
import Endpoints


BearerSession = requests.Session()
BearerSession.headers.update({'Authorization': Credentials.bearerOSEnv()})

print()
# {query: ' place_country:AL'} params wont work without having an ACADEMIC-RESEARCH approved project.
# params = {'query': '"dog" has:media', 'tweet.fields': 'geo,source,entities', 'expansions': '', 'media.fields': 'duration_ms', 'place.fields': 'country,country_code', }

params = {'q': 'BTS -filter:retweets', 'geocode': '35.6897,139.6922,50km', }
BearerSession.params.update(params)
print(BearerSession.params)
# request = requests.request('GET', Endpoints.BaseURL + Endpoints.SearchTweets.Recent,
#                           headers={'Authorization': Credentials.bearerOSEnv()}, params={'query': '😃 boy'})
print(BearerSession)
request = BearerSession.get(Endpoints.BaseURL + Endpoints.Standard.SearchTweets.Recent)

with open('twitter.txt', 'w', encoding='utf-8') as writer:
    writer.write(request.text)

with open('twitter.txt', 'r', encoding='utf-8') as reader:
    for line in reader.readlines():
        print(line)
