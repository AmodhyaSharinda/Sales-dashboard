# data_preprocessing.py

import pandas as pd

def load_and_preprocess_data(file_path):
    # Load CSV file
    data = pd.read_csv(file_path)
    
    # Fill missing values
    data['Product'].fillna('Unknown Product', inplace=True)
    data['Category'].fillna('Unknown Category', inplace=True)
    
    data.dropna(subset=['Date'], inplace=True)  # Remove rows with invalid dates
    
    return data
