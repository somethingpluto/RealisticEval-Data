import pandas as pd

def count_value_frequencies(df, column_name):
    """
    Count the frequency of different values in a specified column of a DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to count values.

    Returns:
    pd.Series: A Series with values and their corresponding frequencies.
    """
    return df[column_name].value_counts()