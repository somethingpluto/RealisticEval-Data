import pandas as pd


def xml_to_dataframe(xml_file: str) -> pd.DataFrame:
    """
    convert the XML file into a pandas DataFrame, where each <sequence>tag is treated as a row record in the XML, and the tag and text content of each sub-element are treated as columns and data of the DataFrame

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        pd.DataFrame: DataFrame containing the data from the XML file.
    """
