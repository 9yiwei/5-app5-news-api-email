import requests
from send_mail import send_mail

api_key = "7679a7ea104b45339327340f29b85ee3"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=7679a7ea104b45339327340f29b85ee3"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    title = article["title"]
    description = article["description"]
    if title is not None:
        body += title + "\n" + description + 2*"\n"

body = body.encode('utf-8')

send_mail(message=body)

