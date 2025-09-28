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
        try:
            data = pd.read_csv(file_path)
            return cls(data)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return None
        except pd.errors.EmptyDataError:
            print("Error: No data found in the file.")
            return None
        except pd.errors.ParserError:
            print("Error: Could not parse the data.")
            return None

    def analyze(self):
        """
        Returns a statistical summary of the data.
        """
        return self.data.describe()