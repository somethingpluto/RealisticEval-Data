import os

def compress_filename(file_name: str, max_length: int = 18) -> str:
    """
    Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension, which defaults to 18 characters.

    For example:
        compress_filename('verylongfilename.txt', 10) output: verylongfi***.txt

    Args:
        file_name (str): The original file name to be compressed.
        max_length (int): The maximum allowed length for the compressed file name. Defaults to 18.

    Returns:
        str: The compressed file name, with the middle section replaced by ellipses ('...'),
              or the original file name if it is within the maximum length.
    """
    if len(file_name) <= max_length:
        return file_name

    filename, file_extension = os.path.splitext(file_name)
    if len(filename) < 5:
        return file_name

    chars_to_keep = max_length - 5
    start_chars = chars_to_keep // 2
    end_chars = chars_to_keep - start_chars

    compressed_name = filename[:start_chars] + '...' + filename[-end_chars:]
    return compressed_name + file_extension
import unittest


class TestCompressFilename(unittest.TestCase):
    def test_return_filename_unchanged_if_under_max_length(self):
        self.assertEqual(compress_filename('file.txt', 10), 'file.txt')

    def test_truncate_and_append_if_exceeds_max_length(self):
        self.assertEqual(compress_filename('verylongfilename.txt', 10), 'verylongfi***.txt')

    def test_preserve_file_extension_after_compression(self):
        self.assertEqual(compress_filename('document.pdf', 5), 'docum***.pdf')

    def test_truncate_and_append_if_filename_exceeds(self):
        self.assertEqual(compress_filename('short.mp3', 2), 'sh***.mp3')
if __name__ == '__main__':
    unittest.main()