import pandas as pd


def dataframe_to_markdown(df):
    """
    Convert a pandas DataFrame to a Markdown table format.

    Args:
    df (pd.DataFrame): The DataFrame to convert.

    Returns:
    str: A string representation of the DataFrame in Markdown table format.
    """
    # Start with an empty list to collect rows
    markdown_lines = []

    # Add the header with alignment (assuming left alignment for simplicity)
    header = "| " + " | ".join(df.columns) + " |"
    markdown_lines.append(header)
    markdown_lines.append("|" + "|".join(['---' * (len(col) // 3 + 1) for col in df.columns]) + "|")

    # Add the data rows
    for index, row in df.iterrows():
        row_str = "| " + " | ".join(str(value) for value in row.values) + " |"
        markdown_lines.append(row_str)

    # Join all lines into a single string
    markdown_str = "\n".join(markdown_lines)
    return markdown_str
