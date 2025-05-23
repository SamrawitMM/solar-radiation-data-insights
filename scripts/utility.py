# scripts/utils.py

import pandas as pd
import os
from scipy.stats import pearsonr, spearmanr


def load_dataset(filename, parse_dates=['Timestamp']) -> pd.DataFrame:
    """
    Load a CSV file with optional country labeling.

    Args:
        file_path (str): Path to the CSV file.
        parse_dates (list): List of date columns to parse. Defaults to ['Timestamp'].


    Returns:
        pd.DataFrame: Loaded DataFrame 
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    file_path = os.path.join(base_path, filename)

    return pd.read_csv(file_path, parse_dates=parse_dates)


def calculate_pearson(df, col1, col2):
    """Calculate and print Pearson correlation coefficient and p-value."""
    corr, p_val = pearsonr(df[col1], df[col2])
    print(f"Pearson correlation between {col1} and {col2}: {corr:.3f} (p={p_val:.3e})")
    return corr, p_val

def calculate_spearman(df, col1, col2):
    """Calculate and print Spearman correlation coefficient and p-value."""
    corr, p_val = spearmanr(df[col1], df[col2])
    print(f"Spearman correlation between {col1} and {col2}: {corr:.3f} (p={p_val:.3e})")
    return corr, p_val