def dataframe_to_markdown(df):
    """
    Converts a pandas DataFrame to a Markdown table format string.

    Args:
    df (pd.DataFrame): The DataFrame to convert.

    Returns:
    str: The Markdown table representation of the DataFrame.
    """
    # Start with the header
    header = "| " + " | ".join(df.columns) + " |\n"
    # Add the separator
    separator = "| " + " | ".join(["---"] * len(df.columns)) + " |\n"
    # Initialize markdown table string
    markdown_table = header + separator

    # Add each row of the DataFrame
    for index, row in df.iterrows():
        row_str = "| " + " | ".join(str(x) for x in row.values) + " |\n"
        markdown_table += row_str

    return markdown_table
