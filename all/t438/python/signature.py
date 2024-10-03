import pandas as pd


def read_csv_to_dataframe(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV file and converts it to a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the data from the CSV file.
    """
