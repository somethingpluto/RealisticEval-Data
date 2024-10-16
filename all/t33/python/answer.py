import pandas as pd
import xml.etree.ElementTree as ET


def parse_xml_to_dataframe(xml_file):
    """
    Convert an XML file into a pandas DataFrame. Each <sequence> tag is treated as a row,
    and each sub-element within <sequence> is treated as a column.

    Args:
    xml_file (str): Path to the XML file.

    Returns:
    pd.DataFrame: DataFrame containing the question from the XML file.
    """
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Prepare a list to hold all rows
    rows = []

    # Iterate over each <sequence> element in the XML file
    for sequence in root.findall('sequence'):
        row_data = {}
        # Iterate over each child of the <sequence> element
        for child in sequence:
            # Use the tag as the column name and the text content as the question
            row_data[child.tag] = child.text
        rows.append(row_data)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(rows)

    return df