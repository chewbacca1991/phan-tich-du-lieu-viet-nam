import pandas as pd

class DataAnalyzer:
    """
    A class to analyze data using pandas.
    """

    def __init__(self, data):
        """
        Initializes the DataAnalyzer with the provided data.
        """
        self.data = data

    @classmethod
    def from_csv(cls, file_path):
        """
        Creates an instance of DataAnalyzer from a CSV file.
        """
        data = pd.read_csv(file_path)
        return cls(data)

    def analyze(self):
        """
        Returns a statistical summary of the data.
        """
        return self.data.describe()