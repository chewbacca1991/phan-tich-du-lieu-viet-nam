import requests

class DataCollector:
    def __init__(self, source):
        self.source = source

    def collect_data(self):
        try:
            response = requests.get(self.source)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f'An error occurred: {e}')
            return None