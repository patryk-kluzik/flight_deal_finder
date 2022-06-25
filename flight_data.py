import datetime
from dateutil.relativedelta import relativedelta
import os
import requests


class FlightData:
    # This class is responsible for structuring the flight data.

    # flight from chosen desitnation (e.g. LON) to places on google sheet
    # only looking for direct flights
    # that leave between tomorrow and 6 months time
    # that are round trips that return between 7 and 14 days
    # currency is GBP
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, from_date, to_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.from_date = from_date
        self.to_date = to_date

    def format_message(self):
        return f"Only £{self.price} to fly from {self.origin_city}-{self.origin_airport} " \
               f"to {self.destination_city}-{self.origin_airport}, from {self.from_date} to {self.to_date}"

    def other_cheapest_flight(self):
        return f"Cheapest flight found is £{self.price} from {self.origin_city}-{self.origin_airport} " \
               f"to {self.destination_city}-{self.origin_airport}, from {self.from_date} to {self.to_date}"