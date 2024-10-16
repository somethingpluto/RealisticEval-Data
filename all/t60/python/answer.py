import os
import pandas as pd
from functools import reduce


def get_common_columns_from_csvs(directory):
    # List to store the DataFrame objects
    dataframes = []

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # Construct the full file path
            filepath = os.path.join(directory, filename)
            # Load the CSV file into a DataFrame
            df = pd.read_csv(filepath)
            # Append the DataFrame to the list
            dataframes.append(df)

    # Use set intersection to find common columns across all DataFrames
    # Start with the columns of the first DataFrame
    if dataframes:
        common_columns = set(dataframes[0].columns)
        # Intersect with columns of each subsequent DataFrame
        for df in dataframes[1:]:
            common_columns.intersection_update(df.columns)
        return list(common_columns)
    else:
        # Return an empty list if no CSV files are found
        return []