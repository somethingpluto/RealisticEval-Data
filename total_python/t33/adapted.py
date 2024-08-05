import pandas as pd
from lxml import etree

def xml_to_dataframe(xml_path):
    """
    Converts an XML file to a pandas DataFrame, where each <sequence> in the XML becomes a row in the DataFrame.

    Args:
    - xml_path (str): The file path of the XML file to be parsed.

    Returns:
    - pd.DataFrame: DataFrame containing the data extracted from the XML file.
    """
    # Load and parse the XML file
    tree = etree.parse(xml_path)
    root = tree.getroot()

    # Collect data from each <sequence> into a list of dictionaries
    rows = [extract_data_from_sequence(seq) for seq in root.findall('sequence')]

    # Convert the list of dictionaries to a DataFrame and return
    return pd.DataFrame(rows)

def extract_data_from_sequence(sequence):
    """
    Extracts data from a <sequence> element to form a single row in the DataFrame.

    Args:
    - sequence (xml.etree.ElementTree.Element): A single <sequence> element from the XML.

    Returns:
    - dict: A dictionary with tags as keys and text as values.
    """
    return {element.tag: element.text for element in sequence}
