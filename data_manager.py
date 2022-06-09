import requests
from requests import request
import os

SHEETY_API = os.environ["SHEETY_API_ENDPOINT"]

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_deal_data = {}


    def get_all_date(self):
        response = requests.get(url=SHEETY_API)
        self.flight_deal_data = response.json()["prices"]
        return self.flight_deal_data

    def update_flight_deal_data(self, data):
        self.flight_deal_data = data

    def update_destination_codes(self):
        for flight in self.flight_deal_data:
            params = {
                "price": {
                    "iataCode": flight["iataCode"]
            }
            }
            response = requests.put(url=f"{SHEETY_API}/{flight['id']}", json=params)
            print(response.text)


