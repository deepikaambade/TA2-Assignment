# data_loader.py

import pandas as pd

def load_data():
    """
    Load datasets from multiple files.

    Prompts the user to specify the number of files to load and their paths. Supports CSV, Excel, and other file formats.

    Returns:
    - dataframes (list of DataFrame): List of loaded DataFrames.
    """
    file_count = int(input("Enter the number of files to load: "))
    dataframes = []

    for i in range(file_count):
        file_path = input(f"Enter the path for file {i + 1}: ")
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            print(f"Unsupported file format: {file_path}")
            continue
        dataframes.append(df)

    return dataframes

if __name__ == "__main__":
    dfs = load_data()
    for i, df in enumerate(dfs):
        print(f"DataFrame {i + 1}:\n", df.head())
