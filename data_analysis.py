import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_csv(cls, file_path):
        data = pd.read_csv(file_path)
        return cls(data)

    def analyze(self):
        return self.data.describe()