# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_all_date()

pprint(sheet_data)

# check if each entry has "IATACODE" populated
for entry in sheet_data:
    if entry["iataCode"] == '':
        flight_search = FlightSearch()
        iata_code = flight_search.get_destination_iata_code(entry["city"])
        entry["iataCode"] = iata_code

pprint(sheet_data)

#
data_manager.update_flight_deal_data(sheet_data)
data_manager.update_destination_codes()