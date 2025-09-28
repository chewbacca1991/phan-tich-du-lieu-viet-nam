import requests

class DataCollector:
    def __init__(self, source):
        self.source = source

    def collect_data(self):
        response = requests.get(self.source)
        return response.json() if response.status_code == 200 else None
