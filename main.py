# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.

import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch

# Get data from Google Sheets using the Sheety API
load_dotenv()
data_manager = DataManager(os.getenv('SHEETY_ENDPOINT'), os.getenv('SHEETY_BEARER_TOKEN'))
sheet_data = data_manager.get_sheet_data()

# To test writing data to Google Sheets, update iataCode column with test data:
for entry in sheet_data:
    if entry['iataCode'] == '':
        flight_search = FlightSearch(os.getenv('TEQUILA_LOCATIONS_ENDPOINT'), os.getenv('TEQUILA_API_KEY'))
        entry['iataCode'] = flight_search.get_iata_code()
        data_manager.update_sheet_data(entry['id'], entry)

# TEST DATA
# sheet_data = [
#   {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2},
#   {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3},
#   {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4},
#   {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5},
#   {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6},
#   {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7},
#   {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8},
#   {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9},
#   {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}
# ]
