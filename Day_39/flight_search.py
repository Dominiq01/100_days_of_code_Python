import os
import requests
from dotenv import load_dotenv

load_dotenv()
AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")
AMADEUS_BEARER = os.environ.get("AMADEUS_BEARER")
class FlightSearch:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {AMADEUS_BEARER}"
        }

    def get_flight_offers(self, origin_iata, destination_iata, departure_date, adults):
        params = {
            "originLocationCode": origin_iata,
            "destinationLocationCode": destination_iata,
            "departureDate": departure_date.strftime("%Y-%m-%d"),
            "adults": str(adults),
        }
        res_flight_offers = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers", params=params, headers=self.headers)
        res_flight_offers.raise_for_status()
        print(res_flight_offers.json())
        flights_data = res_flight_offers.json()
        return flights_data["data"]


    def get_city_iata_code(self, city):
        city_params = {
            "keyword": city
        }
        res_city_data = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities",
                                     params=city_params,
                                     headers=self.headers)
        res_city_data.raise_for_status()
        iata_code = res_city_data.json()["data"][0]["iataCode"]
        return iata_code

    def get_bearer_token(self):
        params = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_API_KEY,
            "client_secret": AMADEUS_API_SECRET
        }

        res = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=params)
        res.raise_for_status()
        bearer_token = res.json()["access_token"]
        print(bearer_token)
        os.environ["AMADEUS_BEARER"] = bearer_token