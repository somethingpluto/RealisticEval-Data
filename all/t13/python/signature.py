from typing import List


def parse_markdown_table(md_table: str) -> List[tuple]:
    """
    Parses a Markdown formatted table into a list of tuples, each tuple representing a row.

    Args:
        md_table (str): A string representing a Markdown table.

    Returns:
        list of tuples: A list where each tuple represents a row in the table.
    """