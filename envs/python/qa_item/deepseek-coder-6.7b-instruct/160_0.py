def compress_filename(file_name: str, max_length: int = 18) -> str:
    """
    Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension.

    Args:
        file_name (str): The original file name to be compressed.
        max_length (int): The maximum allowed length for the compressed file name. Defaults to 18.

    Returns:
        str: The compressed file name, with the middle section replaced by ellipses ('...'),
              or the original file name if it is within the maximum length.
    """
    if len(file_name) <= max_length:
        return file_name

    # Split the filename into name and extension
    name, ext = file_name.rsplit('.', 1)

    # Calculate the length of the name part that can be preserved
    max_name_length = max_length - len(ext) - 1  # -1 for the ellipsis

    # Calculate the length of the preserved parts on each side of the ellipsis
    half_length = max_name_length // 2

    # Construct the compressed filename
    compressed_name = f"{name[:half_length]}...{name[-half_length:]}.{ext}"

    return compressed_name
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