import pandas as pd
import os
import os

# Load the CSV file into a pandas DataFrame
def load_data(csv_path:str='../data/champions_lore.csv'):
    
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(parent_dir, 'data/champions_lore.csv')
    df = pd.read_csv(csv_path)

    return df
