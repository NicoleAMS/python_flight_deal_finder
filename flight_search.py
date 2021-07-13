class FlightSearch:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key
        self.header = {
            "apiKey": self.api_key
        }

    def get_iata_code(self):
        return 'TST'
