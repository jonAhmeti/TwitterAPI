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

The project also uses python to convert data from an excel file to a python Enum class for countries, cities and ISO languages.
Converting countries is done by ExcelToEnumCountries.py which will output a Locations.py file with all the countries taken from worldcities.xlsx
Converting languages is done by LangISO_txt_to_enum.py which outputs a ISO639Lang.py file with all language 639-1 codes and the language names.

The converted Enum classes are all used in the main page for dropdown menus.
For this reason they are also added inside Website > Twitter which is part of installed apps in the Website > settings.py

Once the user submits their search they are able to look at a list/table of results, to see more information they can click on the Details link of the corresponding tweet which will redirect them to the tweet_details/{tweet_id} url where they are able to see a range of information about the tweet and the user.
In case the user changes the link to a different ID that is not saved to our database they will then be redirected to the homepage
