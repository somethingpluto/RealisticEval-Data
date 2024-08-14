import pandas as pd


def fill_na_with_last_valid(df, column_name):
    """
    Populates all NA values in the specified column of the DataFrame with the last valid value.

    Args:
    df (pd.DataFrame): The DataFrame to process.
    column_name (str): The name of the column to fill NA values in.

    Returns:
    pd.DataFrame: The DataFrame with NA values filled in the specified column.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame.")

    # Fill NA with the last valid value in the column using forward fill
    df[column_name] = df[column_name].fillna(method='ffill')

    return df