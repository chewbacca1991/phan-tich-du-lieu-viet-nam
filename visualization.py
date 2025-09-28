import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.data)
        plt.title('Biểu đồ Dữ Liệu')
        plt.show()
