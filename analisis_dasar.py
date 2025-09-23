import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

data = load_data('players_data-2025_2026.csv')
print("Data pemain (5 baris pertama):")
print(data.head())

