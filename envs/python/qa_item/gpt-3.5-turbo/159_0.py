import os

def remove_file_extension(file_name: str) -> str:
    base = os.path.basename(file_name)
    name, _ = os.path.splitext(base)
    return name
import unittest


class TestRemoveFileExtension(unittest.TestCase):
    def test_remove_standard_file_extension(self):
        """Should remove the file extension from a standard file."""
        self.assertEqual(remove_file_extension('document.txt'), 'document')

    def test_return_original_filename_without_extension(self):
        """Should return the original filename for files without an extension."""
        self.assertEqual(remove_file_extension('document'), 'document')

    def test_handle_files_with_multiple_dots(self):
        """Should handle files with multiple dots correctly."""
        self.assertEqual(remove_file_extension('my.file.with.many.extensions.pdf'), 'my.file.with.many.extensions')

    def test_return_original_filename_if_ends_with_dot(self):
        """Should return the original filename if it ends with a dot."""
        self.assertEqual(remove_file_extension('document.'), 'document')

    def test_handle_filenames_with_dots_in_directory_names(self):
        """Should correctly handle filenames with dots in directory names."""
        self.assertEqual(remove_file_extension('path.to/my.file.txt'), 'path.to/my.file')

if __name__ == '__main__':
    unittest.main()