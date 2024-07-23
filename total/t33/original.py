def xml_to_dataframe(xml_path):
    # Parse the XML file
    tree = etree.parse(xml_path)
    root = tree.getroot()

    # Initialize an empty list to store row data
    rows = []

    # Iterate through each sequence in the XML
    for sequence in root.findall('sequence'):
        # Initialize an empty dictionary for each sequence
        row_data = {}

        # Iterate through each child element in the sequence
        for element in sequence:
            # Use tag name as column name and text as the value in the row_data dictionary
            row_data[element.tag] = element.text

        # Append the dictionary to the rows list
        rows.append(row_data)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(rows)

    # Return the DataFrame
    return df