def compress_filename(file_name: str, max_length: int = 18) -> str:
    if len(file_name) <= max_length:
        return file_name
    extension = file_name.split('.')[-1]
    name = file_name.rsplit('.', 1)[0]
    if len(name) + len(extension) > max_length:
        return f"{name[:max_length//2]}...{name[len(name) - max_length//2:]}.{extension}"
    return file_name
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