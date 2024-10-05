import pandas as pd

def fill_missing_with_first_valid(df, column_name):
    """
    Fills missing values in the specified column of the DataFrame with the first valid value in that column.

    :param df: The pandas DataFrame.
    :param column_name: The name of the column to fill missing values.
    :return: The DataFrame with missing values filled.
    """
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")

    # Get the first valid (non-null) value in the specified column
    first_valid_value = df[column_name].dropna().iloc[0] if not df[column_name].dropna().empty else None

    # Fill missing values in the specified column with the first valid value
    df[column_name] = df[column_name].fillna(first_valid_value)

    return df
