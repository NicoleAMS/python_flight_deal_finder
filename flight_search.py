import requests
from flight_data import FlightData


class FlightSearch:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key
        self.header = {
            "apiKey": self.api_key
        }

    def get_iata_code(self, city):
        response = requests.get(url=f"{self.endpoint}/locations/query", headers=self.header, params=city)
        result = response.json()
        iata = result['locations'][0]['code']
        return iata

    def search_flights(self, destination, date_from, date_to):
        params = {
            "fly_from": "AMS",
            "fly_to": destination,
            "date_from": f"{date_from.strftime('%d/%m/%Y')}",
            "date_to": f"{date_to.strftime('%d/%m/%Y')}",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "GBP",
            "one_for_city": 1
        }

        response = requests.get(url=f"{self.endpoint}/v2/search", headers=self.header, params=params)
        result = response.json()

        try:
            data = result['data'][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None
        else:
            flight = FlightData(
                departure_city=data['cityFrom'],
                dep_code=data['flyFrom'],
                destination=data['cityTo'],
                dest_code=data['flyTo'],
                price=data['price'],
                outbound_date=data['route'][0]['local_departure'].split("T")[0],
                return_date=data['route'][1]['local_departure'].split("T")[0]
            )
            print(f"{flight.destination}: £{flight.price}")
            return flight
