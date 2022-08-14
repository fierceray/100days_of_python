# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch

LOCAL_CITY = 'toronto'
local_IATA = 'YYZ'
print(local_IATA)


# TODO 3 if the price is lower than current low price, then send a notificaiton.

def found_lower_price():
    print("found lower price.")


# TODO 1 fetch the required destination city information from sheety API
dm = DataManager()
fs = FlightSearch()
# city_list = dm.data_get()
# for city in city_list:
#     city_id = int(city['id'])
#     dest_IATA_code = city['iataCode']
#     if '' == dest_IATA_code:
#         dest_IATA_code = fs.search_location(city['city'])
#         dm.data_edit(id=city_id, city=city['city'], IATA_code=dest_IATA_code, lowest_price=city['lowestPrice'])
#
#     # TODO 2 use the flight search API from kiwi to search for the cheapest ticket price from local to the destination city
#     # in next 6 months
#
#     current_low_price = city['lowestPrice']
#     try:
#         data = fs.search_flight(origin='CN', destination='YYZ')
#     except IndexError:
#         print("No route found!")
#     else:
#         for each in data:
#             print(each['price'])
#             print(each['deep_link'])
#         # if city['lowestPrice'] > result['price']:
#         #     dm.data_edit(id=city_id, city=city['city'], IATA_code=city['iataCode'], lowest_price=result['price'])
#         #     found_lower_price()

try:
    data = fs.search_flight(origin='CN', destination='YYZ')
except IndexError:
    print("No route found!")
else:
    for index, each in enumerate(data):
        print(each['price'])
        print(each['deep_link'])

        dm.data_edit(id=(index+12), city=each['cityFrom'], IATA_code=each['flyFrom'], lowest_price=each['price'])
