import requests

api_key = "7679a7ea104b45339327340f29b85ee3"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=7679a7ea104b45339327340f29b85ee3"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
