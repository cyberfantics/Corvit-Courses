# import necessary libraries
import requests

# define base URL
base_url = "http://api.openweathermap.org/data/2.5/forecast"

# define parameters
parameters = {"q": "Paris,FR", "appid": "1bf20ea9960dc27c6711a92a66bc51e4"}

# make API request, passing in base URL and parameters
response = requests.get(base_url, params = parameters)

# print out text from API response
print(response.text)