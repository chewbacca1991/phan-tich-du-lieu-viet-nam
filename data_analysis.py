import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        return self.data.describe()
