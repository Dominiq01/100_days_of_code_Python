# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time

from Day_39.data_manager import DataManager
from Day_39.flight_data import FlightData
from Day_39.flight_search import FlightSearch
from datetime import datetime as dt, timedelta

from Day_39.notification_manager import NotificationManager

# Program Requirements
# 1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city.
# Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).
#
# 2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.
#
# 3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.
#
# 4. The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
cities_data = data_manager.get_cities_data()
cities_list = [row["city"] for row in cities_data]
# all_cities_iata_codes = []
#
# for city in cities_list:
#     iata_code = flight_search.get_city_iata_code(city)
#     all_cities_iata_codes.append(iata_code)
#
# curr_row_id = 2
# for code in all_cities_iata_codes:
#     data_manager.edit_row(column_name="iataCode", value=code, row_id=curr_row_id)
#     curr_row_id += 1
#
# print(cities_list)
# print(all_cities_iata_codes)
# flight_search.get_bearer_token()
print(cities_data)
tomorrow_date = dt.today() + timedelta(days=1)
cities_to_change_list = []

for city in cities_data:
    curr_lowest_price = int(city["lowestPrice"])
    flight_data = FlightData(origin_iata="LON", destination_iata=city["iataCode"], departure_date=tomorrow_date,
                             adults_number=1, max_price=curr_lowest_price)
    requested_flights_data = flight_search.get_flight_offers(origin_iata=flight_data.origin_iata,
                                                             destination_iata=flight_data.destination_iata,
                                                             departure_date=flight_data.departure_date,
                                                             adults=flight_data.adults_number)

    cheapest_flight_price = flight_data.find_cheapest_flight(data=requested_flights_data)
    if cheapest_flight_price != curr_lowest_price:
        city["lowestPrice"] = cheapest_flight_price
        cities_to_change_list.append(city)

print(cities_to_change_list)
if cities_to_change_list:
    for city in cities_to_change_list:
        data_manager.edit_row(column_name="lowestPrice", value=city["lowestPrice"], row_id=city["id"])
        notification_manager.send_notification(
            message_to_sent=f"Low price alert! Only €{city["lowestPrice"]} to fly from LON to {city["iataCode"]}, on {tomorrow_date.strftime("%d-%m-%Y")}.")
