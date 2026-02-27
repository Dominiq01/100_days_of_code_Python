import requests
from datetime import datetime as dt
import os
API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
BASE_URL = os.environ.get("BASE_URL")
SHEETY_URL = os.environ.get("SHEETY_URL")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
endpoint_post_exercise = "/v1/nutrition/natural/exercise"

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
user_input = input("Tell me which exercises you did: ")

split_input = user_input.split("and")

for input in split_input:
    data = {
        "query": input,
        "weight": 83,
        "height": 185,
        "age": 24,
        "gender": 'male'
    }

    res = requests.post(url=f"{BASE_URL}{endpoint_post_exercise}", json=data, headers=headers)
    res.raise_for_status()

    res_data = res.json()["exercises"][0]

    today = dt.now().strftime("%d/%m/%Y")
    time = dt.now().time().strftime('%H:%M:%S')


    body = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": res_data["name"].title_class(),
            "duration": res_data["duration_min"],
            "calories": res_data["nf_calories"]
        }
    }

    res_sheety = requests.post(url=SHEETY_URL, json=body, headers=sheety_headers)
    res_sheety.raise_for_status()
    sheety_data = res_sheety.json()
    print(res_data)
    print(sheety_data)
