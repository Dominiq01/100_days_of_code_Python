class FlightData:
    def __init__(self, origin_iata, destination_iata, departure_date, adults_number, max_price):
        self.origin_iata = origin_iata
        self.destination_iata = destination_iata
        self.departure_date = departure_date
        self.adults_number = adults_number
        self.cheapest_flight = max_price

    def find_cheapest_flight(self,data):

        for flight in data:
            curr_flight_price = float(flight["price"]["total"])
            if curr_flight_price < self.cheapest_flight:
                self.cheapest_flight = curr_flight_price

        return self.cheapest_flight
