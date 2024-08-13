import pandas as pd


def dataframe_to_markdown(df: pd.DataFrame):
    """
    convert a DataFrame object to a table in markdown format
    Args:
        df (pd.DataFrame): The DataFrame to convert.

    Returns:
        str: The Markdown table representation of the DataFrame.
    """
