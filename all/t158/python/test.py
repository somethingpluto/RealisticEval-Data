class TestGetFileExtension(unittest.TestCase):

    def test_standard_file_extension(self):
        """should return the file extension for a standard file"""
        self.assertEqual(get_file_extension('example.txt'), 'txt')

    def test_no_extension(self):
        """should return an empty string for files without an extension"""
        self.assertEqual(get_file_extension('example'), '')

    def test_multiple_dots(self):
        """should handle files with multiple dots"""
        self.assertEqual(get_file_extension('example.with.many.dots.jpg'), 'jpg')

    def test_filenames_ending_with_dot(self):
        """should return an empty string for filenames that end with a dot"""
        self.assertEqual(get_file_extension('example.'), '')

    def test_case_sensitivity(self):
        """should correctly handle case sensitivity"""
        self.assertEqual(get_file_extension('example.JPG'), 'JPG')
