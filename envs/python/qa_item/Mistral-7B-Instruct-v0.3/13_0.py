import re
from typing import List

def parse_markdown_table(md_table: str) -> List[tuple]:
    """
    Parses a Markdown formatted table into a list of tuples, each tuple representing a row.

    Args:
        md_table (str): A string representing a Markdown table.

    Returns:
        list of tuples: A list where each tuple represents a row in the table.
    """

    # Find the header row
    header_match = re.search(r'^(.*?)\n', md_table, re.MULTILINE)
    if not header_match:
        return []
    header = header_match.group(1).split('\t')

    # Split the rest of the table into rows
    rows = re.findall(r'^(.*?)\n', md_table[header_match.end():], re.MULTILINE)

    # Convert each row into a tuple and append to the result list
    result = []
    for row in rows:
        row_data = row.split('\t')
        if len(row_data)!= len(header):
            raise ValueError("Inconsistent number of columns")
        result.append(tuple(zip(header, row_data)))

    return result
import unittest


class TestParseMarkdownTable(unittest.TestCase):
    def test_standard_table(self):
        md_table = """
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        | Row1Col1 | Row1Col2 | Row1Col3 |
        | Row2Col1 | Row2Col2 | Row2Col3 |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('Row1Col1', 'Row1Col2', 'Row1Col3'),
            ('Row2Col1', 'Row2Col2', 'Row2Col3')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_inconsistent_columns(self):
        md_table = """
        | Header 1 | Header 2 |
        |----------|----------|
        | Row1     | Row1Col2 | ExtraCol |
        | Row2     |
        """
        expected = [
            ('Header 1', 'Header 2'),
            ('Row1', 'Row1Col2', 'ExtraCol'),
            ('Row2',)
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_empty_cells(self):
        md_table = """
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          | Row1Col2 |          |
        | Row2Col1 |          | Row2Col3 |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('', 'Row1Col2', ''),
            ('Row2Col1', '', 'Row2Col3')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_all_empty_rows(self):
        md_table = """
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          |          |          |
        |          |          |          |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('', '', ''),
            ('', '', '')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_excessive_whitespace(self):
        md_table = """
        |  Header 1  |  Header 2  |  Header 3  |
        |------------|------------|------------|
        |  Row1Col1  |  Row1Col2  |  Row1Col3  |
        |  Row2Col1  |  Row2Col2  |  Row2Col3  |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('Row1Col1', 'Row1Col2', 'Row1Col3'),
            ('Row2Col1', 'Row2Col2', 'Row2Col3')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)


def parse_markdown_table(md_table):
    """
    Parses a Markdown formatted table into a list of tuples, each tuple representing a row.

    Args:
        md_table (str): A string representing a Markdown table.

    Returns:
        list of tuples: A list where each tuple represents a row in the table.
    """
    # Split the input string into lines and strip whitespace
    lines = md_table.strip().split('\n')

    # Filter out the separator line for the header (which usually contains "---")
    lines = [line for line in lines if not line.strip().startswith('|---')]

    # Initialize the list to store each row as a tuple
    table_data = []

    # Process each line
    for line in lines:
        # Strip leading and trailing spaces and pipes, then split by "|"
        row = line.strip('| \n').split('|')
        # Strip spaces from each cell, handle empty cells, and create a tuple
        table_data.append(tuple(cell.strip() for cell in row if cell.strip() or cell == ''))

    return table_data

if __name__ == '__main__':
    unittest.main()