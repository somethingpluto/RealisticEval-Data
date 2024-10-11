import pandas as pd


def dataframe_to_markdown(df: pd.DataFrame, md_path: str) -> str:
    """
    convert a DataFrame object to a table in markdown format
    For example:
        input: dataframe {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        output: | Name | Age |\n| --- | --- |\n| Alice | 25 |\n| Bob | 30 |\n

    Args:
        df (DataFrame): DataFrame type question
        md_path (str): output md file path

    Returns:
        markdown file content str
    """
