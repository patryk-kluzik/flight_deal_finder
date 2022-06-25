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
    flight_search = FlightSearch()
    if entry["iataCode"] == '':
        iata_code = flight_search.get_destination_iata_code(city_name=entry["city"])
        entry["iataCode"] = iata_code

    cheapest_flights = flight_search.perform_search(destination_code=entry["iataCode"])

    try:
        for flight in cheapest_flights:
            if flight.price <= entry["lowestPrice"]:
                pprint(flight.format_message())
            else:
                pprint(f"No flights below £{entry['lowestPrice']}! {flight.other_cheapest_flight()}")
    except:
        pass

pprint(sheet_data)

# #
# data_manager.update_flight_deal_data(sheet_data)
# data_manager.update_destination_codes()
