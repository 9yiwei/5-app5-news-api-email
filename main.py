import requests
from send_mail import send_mail

topic = "tesla"
api_key = "7679a7ea104b45339327340f29b85ee3"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&sortBy=publishedAt&" \
      "apiKey=7679a7ea104b45339327340f29b85ee3&" \
      "language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n" \
                + article["description"] + "\n" \
                + article["url"] + 2*"\n"


body = ("Subject: Today's news" + "\n" + body).encode('utf-8')

send_mail(message=body)

