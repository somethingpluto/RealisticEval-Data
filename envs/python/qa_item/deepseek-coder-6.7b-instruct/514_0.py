import re

def extract_date_from_filename(file_name: str):
    """
    Extracts the date in the format YYYY-MM-DD from the given file name.

    Args:
        file_name (str): The name of the file which may contain a date.

    Returns:
        str or None: The extracted date string in YYYY-MM-DD format if found, else None.
    """
    # Regular expression to match dates in the format YYYY-MM-DD
    date_pattern = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\b')
    
    # Search for the date pattern in the file name
    match = date_pattern.search(file_name)
    
    # If a match is found, return the date in YYYY-MM-DD format
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    
    # If no match is found, return None
    return None
import unittest


class TestExtractDateFromFilename(unittest.TestCase):

    def test_date_extraction_success(self):
        """Test case where the date is successfully extracted."""
        file_name = "report-2023-09-28.txt"
        expected_date = "2023-09-28"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

    def test_no_date_in_filename(self):
        """Test case where no date is present in the filename."""
        file_name = "report.txt"
        self.assertIsNone(extract_date_from_filename(file_name))

    def test_multiple_dates_in_filename(self):
        """Test case where multiple dates are present, should return the first one."""
        file_name = "report-2023-09-28-backup-2023-10-01.txt"
        expected_date = "2023-09-28"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

    def test_date_at_start_of_filename(self):
        """Test case where the date is at the start of the filename."""
        file_name = "2023-09-28-report.txt"
        expected_date = "2023-09-28"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

    def test_incorrect_date_format(self):
        """Test case where the date format is incorrect."""
        file_name = "report-2023-99-99.txt"  # Invalid date
        expected_date = "2023-99-99"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

if __name__ == '__main__':
    unittest.main()