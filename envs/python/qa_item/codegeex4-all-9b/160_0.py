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
    import os

    if len(file_name) <= max_length:
        return file_name

    name, extension = os.path.splitext(file_name)
    name_length = max_length - len(extension) - 3  # 3 for the ellipsis (...)

    if name_length <= 0:
        return file_name

    start = name[:name_length // 2]
    end = name[-(name_length - name_length // 2):]
    compressed_name = f"{start}***{end}{extension}"
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