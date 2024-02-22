import pandas as pd
import os

# Load the CSV file into a pandas DataFrame
def load_data(csv_path:str='../data/champions_lore.csv'):

    df = pd.read_csv(csv_path)

    return df
