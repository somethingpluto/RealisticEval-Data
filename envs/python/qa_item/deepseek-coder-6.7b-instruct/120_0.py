from typing import List
from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.current_row = []
        self.table_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        elif tag == 'tr':
            self.in_row = True
            self.current_row = []
        elif tag == 'td' or tag == 'th':
            self.in_cell = True

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        elif tag == 'tr':
            self.in_row = False
            if self.current_row:
                self.table_data.append(self.current_row)
        elif tag == 'td' or tag == 'th':
            self.in_cell = False

    def handle_data(self, data):
        if self.in_cell:
            self.current_row.append(data.strip())

def extract_csv_data_from_html(html_content: str) -> List[List[str]]:
    parser = TableParser()
    parser.feed(html_content)
    return parser.table_data
import unittest


class TestHTMLToCSVExtraction(unittest.TestCase):

    def test_table_with_multiple_rows_and_columns(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Cell 1</td><td>Cell 2</td></tr>
                <tr><td>Cell 3</td><td>Cell 4</td></tr>
            </tbody>
        </table>
        """
        expected = [["Cell 1", "Cell 2"], ["Cell 3", "Cell 4"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_empty_cells(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Cell 1</td><td></td></tr>
                <tr><td></td><td>Cell 4</td></tr>
            </tbody>
        </table>
        """
        expected = [["Cell 1", ""], ["", "Cell 4"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_only_one_row(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Single Cell 1</td><td>Single Cell 2</td></tr>
            </tbody>
        </table>
        """
        expected = [["Single Cell 1", "Single Cell 2"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_only_one_column(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Column Cell 1</td></tr>
                <tr><td>Column Cell 2</td></tr>
            </tbody>
        </table>
        """
        expected = [["Column Cell 1"], ["Column Cell 2"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_no_table_with_class_waffle_present(self):
        test_case_html = """
        <div>
            <p>No table here!</p>
        </div>
        """
        expected = []
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

if __name__ == '__main__':
    unittest.main()