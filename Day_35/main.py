import requests
from twilio.rest import Client
import os
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
phone_num = os.environ["PHONE_NUMBER"]

lat = 41.867129
lng = 12.530556
API_KEY = os.environ.get("OWM_API_KEY")
params = {
    "lat": lat,
    "lon": lng,
    "appid": API_KEY,
    "cnt": 4
}
res =  requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=params)
res.raise_for_status()
data = res.json()["list"]

weather_list = [forecast["weather"] for forecast in data]
condition_id_list = [int(weather[0]["id"]) for weather in weather_list]
print(condition_id_list)

if any(id < 600 for id in condition_id_list):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MGc6d68bebf546d2b022d06a7aac5558b3',
        body="Bring an umbrella ☂️, it's raining man...",
        to=phone_num
    )
