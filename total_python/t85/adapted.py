import pandas as pd


def naive_ffill(df: pd.DataFrame, column: str) -> None:
    """
    Forward fills missing values in a specified column of a pandas DataFrame using a naive method.

    Args:
    df (pd.DataFrame): The DataFrame containing the data.
    column (str): The name of the column in which to forward fill missing values.

    Returns:
    None: The function modifies the DataFrame in place.

    Raises:
    KeyError: If the specified column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")

    last_valid = None
    for idx, value in df[column].items():
        if pd.isna(value):
            df.loc[idx, column] = last_valid
        else:
            last_valid = value