from twilio.rest import Client
import requests
from newsapi import NewsApiClient
import os

API_KEY_ALPHA = os.environ.get("ALPHA_VANTAGE_KEY")
API_KEY_NEWS = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_NUM = os.environ["PHONE_NUMBER"]

SYMBOL = "BTC"
CURRENCY_NAME = "bitcoin"
MY_PERCENT_DIFF = 10

params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": SYMBOL,
    "market": "USD",
    "apikey": API_KEY_ALPHA
}

url = 'https://www.alphavantage.co/query'
res = requests.get(url, params)
res.raise_for_status()
data = res.json()["Time Series (Digital Currency Daily)"]
data_list  = [value for index, value in data.items()][:2]

price_yesterday = float(data_list[0]["4. close"])
price_two_days_ago = float(data_list[1]["4. close"])

avg =  (price_yesterday + price_two_days_ago) / 2
percent_diff = 100 * (price_yesterday - price_two_days_ago) / avg

print(percent_diff)

if percent_diff < -MY_PERCENT_DIFF or percent_diff > MY_PERCENT_DIFF:
    newsapi = NewsApiClient(api_key=API_KEY_NEWS)

    top_headlines = newsapi.get_everything(q=CURRENCY_NAME)["articles"][:3]

    # print(top_headlines)
    if percent_diff < -MY_PERCENT_DIFF:
        sign = "📉"
    else:
        sign = "📈"

    message_to_sent = f"{SYMBOL}:{sign} {round(percent_diff, 2)}%\n"
    for article in top_headlines:
        message_to_sent += f"\nHeadline: {article["title"]}\nBrief: {article["description"]}\n{article["url"]}\n"
    # print(message_to_sent)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_to_sent,
        to=f'whatsapp:{PHONE_NUM}'
    )