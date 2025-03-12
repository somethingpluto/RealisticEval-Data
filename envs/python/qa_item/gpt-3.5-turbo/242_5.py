from typing import List, Dict

def classify_files_by_extension(file_names: List[str]) -> Dict:
    extensions_dict = {}
    for file_name in file_names:
        file_parts = file_name.split('.')
        if len(file_parts) > 1:
            extension = file_parts[-1]
            if extension in extensions_dict:
                extensions_dict[extension].append(file_name)
            else:
                extensions_dict[extension] = [file_name]
    return extensions_dict
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