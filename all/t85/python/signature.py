import pandas
import pandas as pd


def fill_missing_with_first_valid(df: pandas.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Fills missing values in the specified column of the DataFrame with the first valid value in that column.
    Args:
        df (pandas.DataFrame): The pandas DataFrame.
        column_name (str): The name of the column to fill missing values.

    Returns:
        pd.DataFrame: The DataFrame with missing values filled.
    """
