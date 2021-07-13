import requests

class FlightSearch:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key
        self.header = {
            "apiKey": self.api_key
        }
        self.iata = ""

    def get_iata_code(self, query):
        response = requests.get(url=self.endpoint, headers=self.header, params=query)
        result = response.json()
        iata = result['locations'][0]['code']
        self.iata = iata
        return iata
