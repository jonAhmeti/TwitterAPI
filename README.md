# TwitterAPI
Project uses the Standard v1.1 Twitter API

This project uses Django framework v3.0.13 and Requests: HTTP for Humans™ library.
Django is used to create a website using views, templates, forms and models.
It is connected to Microsoft SQL Server locally where the tweets and users are saved.
You're able to use the API from going to localhost:8000/ which is the homepage.
There you NEED to at least fill the text query for looking up tweets.
Other inputs: Language, Type, Count, Country, City, Radius are optional.

Default values: 
  Type = mixed
  Count = 1
  
Other inputs that have no value won't be passed as url parameters to the endpoint.
Only recent tweets are searched, meaning the API Endpoint https://api.twitter.com/1.1/search/tweets.json

The authorization credentials are saved in the OS environment and authorization is done using Bearer token.
It can be found under Project > Website > Tweets > API
Inside API there are three folders Endpoints where the twitter's base url is saved and the search tweets API endpoint.
Inside API there's a class called SearchTweets which is used to contact the API.
SearchTweets has two methods: 
  set_params(**kwargs), this method accepts a dictionary-like object from which the parameters will be set.
  send(), is the method which prepares the request and sends a PreparedRequest with some data also saved in the Session. It returns a Response object.
  
