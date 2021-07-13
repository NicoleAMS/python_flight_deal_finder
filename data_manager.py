import requests


class DataManager:
    def __init__(self, endpoint, token):
        self.endpoint = endpoint
        self.bearer_token = f"Bearer {token}"
        self.header = {
            "Content-Type": "application/json",
            "Authorization": self.bearer_token
        }
        self.data = []

    def get_sheet_data(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        result = response.json()
        self.data = result['prices']
        return result['prices']

    def update_sheet_data(self, row_id, payload):
        url = f"{self.endpoint}/{row_id}"
        body = {
            "price": {key: payload[key] for key in payload}
        }
        response = requests.put(url=url, json=body, headers=self.header)
        result = response.json()
        print(result)
