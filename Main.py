import Credentials
import requests
import Endpoints

BearerSession = requests.Session()
BearerSession.headers.update({'Authorization': Credentials.bearerOSEnv()})

print()

BearerSession.params.update({'query': '😃 boy'})
# request = requests.request('GET', Endpoints.BaseURL + Endpoints.SearchTweets.Recent,
#                           headers={'Authorization': Credentials.bearerOSEnv()}, params={'query': '😃 boy'})

request = BearerSession.get(Endpoints.BaseURL + Endpoints.SearchTweets.Recent)

with open('twitter.txt', 'w', encoding='utf-8') as writer:
    writer.write(request.text)
