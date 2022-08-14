import requests
from _datetime import datetime, timedelta

API_KEY = '21gzQ8nLRAyYhaRYOvRSDsqKo9v5GjU9'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.headers = {
            'accept': 'application / json',
            'apikey': API_KEY,
        }

    def search_location(self, term: str):
        ENDPOINT_location = 'https://tequila-api.kiwi.com/locations/query'
        parameters = {
            'term': term,
            'locale': 'en - US',
            'location_types': 'city',
            'limit': '10',
            'active_only': 'true',
        }

        response = requests.get(url=ENDPOINT_location, params=parameters, headers=self.headers)
        return response.json()['locations'][0]['code']

    def search_flight(self, origin, destination):
        today = datetime.now()
        ENDPOINT_search = 'https://tequila-api.kiwi.com/v2/search'
        parameters = {
            'fly_from': origin,
            'fly_to': destination,
            'date_from': today.strftime("%d/%m/%Y"),
            'date_to': (today + timedelta(days=180)).strftime("%d/%m/%Y"),
            'return_from': (today + timedelta(days=7)).strftime("%d/%m/%Y"),
            'return_to': (today + timedelta(days=187)).strftime("%d/%m/%Y"),
            'max_fly_duration': '20',
            'flight_type': 'oneway',
            'one_for_city': '0',
            'one_per_date': '0',
            'adults': '1',
            'only_working_days': 'false',
            'only_weekends': 'false',
            'partner_market': 'us',
            'max_stopovers': '0',
            'max_sector_stopovers': '2',
            'vehicle_type': 'aircraft',
            'limit': '500',
            'curr': 'CAD',
        }
        response = requests.get(url=ENDPOINT_search, params=parameters, headers=self.headers)
        print("In the search flight")
        data = response.json()['data']
        print(data)
        return data


if __name__ == '__main__':
    FlightSearch().search_location('guangzhou')
    FlightSearch().search_flight()
