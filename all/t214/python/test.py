class TestReadMappingFile(unittest.TestCase):

    def setUp(self):
        # Create a temporary mapping file for testing
        self.valid_file_path = 'valid_mapping.txt'
        self.invalid_file_path = 'invalid_mapping.txt'
        self.empty_file_path = 'empty_mapping.txt'

        # Valid file content
        with open(self.valid_file_path, 'w') as f:
            f.write("'pattern1','replacement1'\n")
            f.write("'pattern2','replacement2'\n")

        # Invalid file content
        with open(self.invalid_file_path, 'w') as f:
            f.write("'pattern1'\n")  # Missing replacement
            f.write("'pattern2','replacement2'\n")

        # Empty file
        open(self.empty_file_path, 'w').close()  # Create an empty file

    def tearDown(self):
        # Remove temporary files after tests
        for file_path in [self.valid_file_path, self.invalid_file_path, self.empty_file_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_valid_file(self):
        """Test reading a valid mapping file."""
        expected_result = [
            (re.compile("pattern1"), 'replacement1'),
            (re.compile("pattern2"), 'replacement2'),
        ]
        result = read_mapping_file(self.valid_file_path)
        self.assertEqual(result, expected_result)

    def test_file_not_found(self):
        """Test for FileNotFoundError when the file does not exist."""
        with self.assertRaises(FileNotFoundError):
            read_mapping_file('non_existent_file.txt')

    def test_invalid_mapping_format(self):
        """Test for ValueError when the file has an invalid mapping format."""
        with self.assertRaises(ValueError):
            read_mapping_file(self.invalid_file_path)

    def test_empty_file(self):
        """Test for an empty file, expecting an empty list."""
        result = read_mapping_file(self.empty_file_path)
        self.assertEqual(result, [])

    def test_leading_trailing_spaces(self):
        """Test handling of leading/trailing spaces around patterns and replacements."""
        with open('spaced_mapping.txt', 'w') as f:
            f.write(" ' pattern1 ' , ' replacement1 ' \n")
            f.write(" ' pattern2 ' , ' replacement2 ' \n")

        expected_result = [
            (re.compile("pattern1"), 'replacement1'),
            (re.compile("pattern2"), 'replacement2'),
        ]
        result = read_mapping_file('spaced_mapping.txt')
        self.assertEqual(result, expected_result)
        os.remove('spaced_mapping.txt')