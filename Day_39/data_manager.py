import os
import requests
from dotenv import load_dotenv

load_dotenv()
SHEETY_BEARER = os.environ.get("SHEETY_BEARER")

class DataManager:
    def __init__(self, first_row_id = 2):
        self.headers = {
            "Authorization": f"Bearer {SHEETY_BEARER}"
        }
        self.first_row_id = first_row_id

    def get_cities_data(self):
        res_cities = requests.get("https://api.sheety.co/3e22a110c5fcb3109db1cf8f410176ec/flightDeals/prices",
                                  headers=self.headers)
        res_cities.raise_for_status()
        data = res_cities.json()["prices"]
        return data

    def edit_row(self, column_name, value, row_id):
        sheety_data = {
            "price": {
                f"{column_name}": value
            }
        }
        res_sheety = requests.put(
            f"https://api.sheety.co/3e22a110c5fcb3109db1cf8f410176ec/flightDeals/prices/{row_id}",
            json=sheety_data,
            headers=self.headers)
        res_sheety.raise_for_status()
        print(res_sheety.text)