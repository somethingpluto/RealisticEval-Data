import pandas as pd

def naive_ffill(df, column):
    """
    Forward fills the missing values in a specified column of a DataFrame using the last valid value.

    Args:
    df (pd.DataFrame): The DataFrame to process.
    column (str): The name of the column in which to fill missing values.

    Returns:
    None: Modifies the DataFrame in place.

    Raises:
    KeyError: If the specified column does not exist in the DataFrame.
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame.")

    last_valid = None
    for idx, value in df[column].iteritems():  # use iteritems() for compatibility
        if pd.isna(value):
            df.at[idx, column] = last_valid
        else:
            last_valid = value