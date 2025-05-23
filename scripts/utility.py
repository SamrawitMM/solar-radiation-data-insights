# scripts/utils.py

import pandas as pd

def load_dataset(file_path: str, parse_dates: list = ['Timestamp']) -> pd.DataFrame:
    """
    Load a CSV file with optional country labeling.

    Args:
        file_path (str): Path to the CSV file.
        parse_dates (list): List of date columns to parse. Defaults to ['Timestamp'].


    Returns:
        pd.DataFrame: Loaded DataFrame 
    """
    df = pd.read_csv(file_path, parse_dates=parse_dates)
    
    return df
