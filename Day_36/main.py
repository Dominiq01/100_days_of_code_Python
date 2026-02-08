from twilio.rest import Client
import requests
from datetime import datetime as dt
import datetime
from newsapi import NewsApiClient

STOCK = "NVDA"
COMPANY_NAME = "Nvidia"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": 2,
    "apikey": "API_KEY"
}

url = 'https://www.alphavantage.co/query'
res = requests.get(url, params)
res.raise_for_status()
data = res.json()["Time Series (Daily)"]
today = dt.now().date()
day_of_week = dt.now().weekday()
print(day_of_week)


if day_of_week == 6:
    yesterday = str(today - datetime.timedelta(days=2))
    two_days_ago = str(today - datetime.timedelta(days=3))
else:
    yesterday = str(today - datetime.timedelta(days=1))
    two_days_ago = str(today - datetime.timedelta(days=2))
print(yesterday)
print(two_days_ago)

data_to_analyse = { date: float(value["4. close"]) for date, value in data.items() if date == two_days_ago or date == yesterday}

price_yesterday = data_to_analyse[yesterday]
price_two_days_ago = data_to_analyse[two_days_ago]

print(price_yesterday - price_two_days_ago)
avg =  (price_yesterday + price_two_days_ago) / 2
percent_diff = 100 * (price_yesterday - price_two_days_ago) / avg
print(data)
print(data_to_analyse)
print(percent_diff)

if percent_diff < -5 or percent_diff > 5:
    newsapi = NewsApiClient(api_key="API_KEY_NEWS")

    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                              category='business')["articles"][:3]

    print(top_headlines)
    if percent_diff < -5:
        sign = "📉"
    else:
        sign = "📈"

    message = f"{STOCK}:{sign} {round(percent_diff, 2)}%\n"
    for article in top_headlines:
        message += f"Headline: {article["title"]}\nBrief: {article["description"]}\n"
    print(message)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

