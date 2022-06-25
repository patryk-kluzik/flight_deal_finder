import os
import datetime
from dateutil.relativedelta import relativedelta
import requests

from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.KIWI_API_ENDPOINT = 'https://tequila-api.kiwi.com'
        self.api_key = os.environ["KIWI_API_KEY"]
        self.iata_code = ''

    def get_destination_iata_code(self, city_name):
        query_params = {
            "term": city_name
        }
        auth_header = {
            "apikey": f'{self.api_key}/locations/query'
        }
        response = requests.get(url=self.KIWI_API_ENDPOINT, headers=auth_header, params=query_params)
        self.iata_code = response.json()["locations"][0]["code"]
        return self.iata_code

    def perform_search(self, destination_code, departure_code="LHR"):
        auth_header = {
            "apikey": self.api_key
        }
        query_params = {
            "fly_from": departure_code,
            "fly_to": destination_code,
            "date_from": (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(url=f'{self.KIWI_API_ENDPOINT}/v2/search', params=query_params, headers=auth_header)

        try:
            data = response.json()["data"]  # get a list of all flights
            first = data[0]
        except IndexError:
            print(f"No flights found for {destination_code}")
            return None

        lowest_price = min(flight["price"] for flight in data)  # get the cheapest flight
        # index of all flights that are the cheapest
        cheapest_flights = [flight for idx, flight in enumerate(data) if flight["price"] == lowest_price]
        print(len(cheapest_flights))
        cheapest_flights_class = []
        for flight in cheapest_flights:
            flight_data = FlightData(
                price=flight["price"],
                origin_city=flight["cityFrom"],
                origin_airport=flight["flyFrom"],
                destination_city=flight["cityTo"],
                destination_airport=flight["flyTo"],
                from_date=flight["route"][0]["local_departure"].split("T")[0],
                to_date=flight["route"][1]["local_departure"].split("T")[0]
            )
            cheapest_flights_class.append(flight_data)

        return cheapest_flights_class
