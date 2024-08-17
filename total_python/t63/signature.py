import pandas as pd


def dataframe_to_markdown(df: pd.DataFrame, md_path: str) -> str:
    """
    convert a DataFrame object to a table in markdown format
    Args:
        df (DataFrame): DataFrame type data
        md_path (str): output md file path

    Returns:
        markdown file content str
    """
