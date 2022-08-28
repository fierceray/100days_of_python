import requests


ENDPOINT_sheety = 'https://api.sheety.co/39076523cfe1a047a0a40f52ffaa5ec8/flightDeals/prices'
TOKEN = 'app used to track flight, all in capital'

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.headers = {
            'Authorization': f'Bearer {TOKEN}',
        }


    def data_get(self):
        response = requests.get(url=ENDPOINT_sheety, headers=self.headers)
        response.raise_for_status()
        return response.json()['prices']

    def data_edit(self, id, city, IATA_code, lowest_price):
        body = {
            'price': {
                'city': city,
                'iataCode': IATA_code,
                'lowestPrice': lowest_price,
            }
        }
        response = requests.put(url=f"{ENDPOINT_sheety}/{id}", headers=self.headers, json=body)
        print("In the data edit")
        print(response.json())


if __name__ == '__main__':

    DataManager().data_edit()
    DataManager().data_get()
