from . import Credentials
from . import Endpoints
import requests


class SearchTweets:
    def __init__(self):
        self.session_bearer = requests.Session()
        self.session_bearer.headers.update({'Authorization': Credentials.bearerOSEnv()})
        self.request = requests.Request(method='GET', url=Endpoints.BaseURL + Endpoints.Standard.SearchTweets)

    def set_params(self, **kwargs):
        params = {}
        for (key, value) in kwargs.items():
            if value != '':
                params.update({key: value})

        print(f'kwargs: {kwargs}\n\n')
        self.session_bearer.params.update(params)
        print(f'Session_Request params: {self.session_bearer.params}\n\n')
        print(f'HEADERS: {self.session_bearer.headers}')

    def send(self):
        self.request.headers.update(self.session_bearer.headers)
        self.request.params.update(self.session_bearer.params)
        self.request = self.request.prepare()
        return self.session_bearer.send(self.request)


# params = {'q': 'BTS -filter:retweets', 'geocode': '35.6897,139.6922,50km', }
# BearerSession.params.update(params)
# print(BearerSession.params)
# # request = requests.request('GET', Endpoints.BaseURL + Endpoints.SearchTweets.Recent,
# #                           headers={'Authorization': Credentials.bearerOSEnv()}, params={'query': '😃 boy'})
# print(BearerSession)
# request = BearerSession.get(Endpoints.BaseURL + Endpoints.Standard.SearchTweets)
#
# with open('twitter.txt', 'w', encoding='utf-8') as writer:
#     writer.write(request.text)
#
# with open('twitter.txt', 'r', encoding='utf-8') as reader:
#     for line in reader.readlines():
#         print(line)
