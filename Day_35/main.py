import requests
from twilio.rest import Client
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
phone_num = os.environ["PHONE_NUMBER"]
API_KEY = os.environ["OWM_API_KEY"]

# Wadowice (34-100), ul. Krakowska, Poland. Forecasts are city-level, so the street
# uses the same coordinates as the rest of town.
lat = 49.8838
lng = 19.4933

params = {
    "lat": lat,
    "lon": lng,
    "appid": API_KEY,
    "cnt": 4
}
res = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=params, timeout=30)
res.raise_for_status()
data = res.json()["list"]

weather_list = [forecast["weather"] for forecast in data]
condition_id_list = [int(weather[0]["id"]) for weather in weather_list]
print(condition_id_list)

# OpenWeatherMap condition ids below 600 are thunderstorm / drizzle / rain.
if any(cid < 600 for cid in condition_id_list):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MGc6d68bebf546d2b022d06a7aac5558b3',
        body="Weź parasol ☂ dziś będzie padać",
        to=phone_num
    )
    print(f"SMS sent (sid: {message.sid})")
else:
    print("No rain expected. No SMS sent.")
