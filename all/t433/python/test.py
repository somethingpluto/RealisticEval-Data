import os
import unittest


class TestReadParagraphs(unittest.TestCase):
    def setUp(self):
        """Create sample files for testing."""
        self.test_files = {
            "file1.txt": "This is the first paragraph.\nIt has two lines.\n\nThis is the second paragraph.\nIt has one line.",
            "file2.txt": "Single paragraph with no newlines.\nJust one line.\n\n\nSecond paragraph here.",
            "file3.txt": "Paragraph one.\n\nParagraph two.\n\nParagraph three with two lines.\nThis is the second line.",
            "file4.txt": "\n\n\n\nMultiple empty paragraphs.\n\n\n\n",
            "file5.txt": ""
        }

        for filename, content in self.test_files.items():
            with open(filename, 'w') as f:
                f.write(content)

    def tearDown(self):
        """Remove the test files after tests are complete."""
        for filename in self.test_files.keys():
            if os.path.exists(filename):
                os.remove(filename)

    def test_case1(self):
        """Test with a standard file containing multiple paragraphs."""
        expected_output = [
            ["This is the first paragraph.", "It has two lines."],
            ["This is the second paragraph.", "It has one line."]
        ]
        self.assertEqual(read_paragraphs("file1.txt"), expected_output)

    def test_case2(self):
        """Test with a file that has a single paragraph with no double newlines."""
        expected_output = [
            ["Single paragraph with no newlines.", "Just one line."],
            [""]
        ]
        self.assertEqual(read_paragraphs("file2.txt"), expected_output)

    def test_case3(self):
        """Test with a file containing multiple paragraphs with varying lengths."""
        expected_output = [
            ["Paragraph one."],
            ["Paragraph two."],
            ["Paragraph three with two lines.", "This is the second line."]
        ]
        self.assertEqual(read_paragraphs("file3.txt"), expected_output)

    def test_case4(self):
        """Test with a file containing multiple empty paragraphs."""
        expected_output = [
            ["", "", "", ""],
            ["Multiple empty paragraphs."],
            ["", "", "", ""]
        ]
        self.assertEqual(read_paragraphs("file4.txt"), expected_output)

    def test_case5(self):
        """Test with an empty file."""
        expected_output = [[]]
        self.assertEqual(read_paragraphs("file5.txt"), expected_output)