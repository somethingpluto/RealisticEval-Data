
from typing import List, Dict

def classify_files_by_extension(file_names: List[str]) -> Dict:
    """
    Classify an array of file names according to their file extensions.

    Args:
        file_names: List of file names (strings).

    Returns:
        Dict: Dictionary with file extensions as keys and lists of file names as values.
    """
    # Create a dictionary to store the classification
    classification = {}

    # Iterate over the file names and classify them
    for file_name in file_names:
        # Check if the file name is in the dictionary
        if file_name in classification:
            # If it is, add the file name to the list of classified files
            classification[file_name] = [f for f in file_names if f.endswith(file_name)]
        else:
            # If it isn't, add the file name to the list of classified files
            classification[file_name] = [f for f in file_names if f.endswith(file_name)]

    # Return the dictionary
    return classification

import unittest


class TestClassifyFilesByExtension(unittest.TestCase):

    def test_multiple_file_types(self):
        """Test with multiple file types."""
        files = [
            "document.docx",
            "photo.jpeg",
            "report.pdf",
            "image.png",
            "archive.zip"
        ]
        expected_result = {
            'docx': ['document.docx'],
            'jpeg': ['photo.jpeg'],
            'pdf': ['report.pdf'],
            'png': ['image.png'],
            'zip': ['archive.zip']
        }
        self.assertEqual(classify_files_by_extension(files), expected_result)

    def test_empty_list(self):
        """Test with an empty list of file names."""
        files = []
        expected_result = {}
        self.assertEqual(classify_files_by_extension(files), expected_result)

    def test_files_with_same_extension(self):
        """Test with multiple files having the same extension."""
        files = [
            "file1.txt",
            "file2.txt",
            "file3.txt",
        ]
        expected_result = {
            'txt': [
                "file1.txt",
                "file2.txt",
                "file3.txt",
            ]
        }
        self.assertEqual(classify_files_by_extension(files), expected_result)

    def test_files_with_multiple_dots(self):
        """Test files that have multiple dots in their names."""
        files = [
            "my.document.docx",
            "report.final.pdf",
            "photo.album.jpeg",
            "archive.backup.zip"
        ]
        expected_result = {
            'docx': ['my.document.docx'],
            'pdf': ['report.final.pdf'],
            'jpeg': ['photo.album.jpeg'],
            'zip': ['archive.backup.zip']
        }
        self.assertEqual(classify_files_by_extension(files), expected_result)
if __name__ == '__main__':
    unittest.main()