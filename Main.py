import Credentials
import requests
import Endpoints


request = requests.request('GET', Endpoints.BaseURL + Endpoints.SearchTweets.Recent,
                           headers={'Authorization': Credentials.bearerOSEvn()}, params={'query': '😃 boy'})


with open('twitter.txt', 'w', encoding='utf-8') as writer:
    writer.write(request.text)

