import hashlib
import unittest
from unittest.mock import patch, mock_open, MagicMock, call


class TestHashDirectory(unittest.TestCase):
    def setUp(self):
        # Sample file data to simulate file reads
        self.file_data = {
            '/fake/dir/file1.txt': b'Hello, world!',
            '/fake/dir/file2.txt': b'Goodbye, world!'
        }

        # Fake directory walk to simulate os.walk
        self.fake_walk = [
            ('/fake/dir', ('subdir',), ('file1.txt', 'file2.txt')),
            ('/fake/dir/subdir', (), ('file3.txt',)),
        ]

        # Mock for os.walk
        self.patcher_walk = patch('os.walk', return_value=self.fake_walk)
        self.mock_walk = self.patcher_walk.start()

        # Mock for open
        self.patcher_open = patch('builtins.open', mock_open())
        self.mock_open = self.patcher_open.start()

    def tearDown(self):
        self.patcher_walk.stop()
        self.patcher_open.stop()

    @patch('hashlib.sha256')
    def test_all_files_hashed(self, mock_hash):
        # Setup mock hashlib to avoid actual file hashing
        mock_hash.return_value.hexdigest.return_value = 'dummyhash'

        # Mock read behavior based on file path
        def side_effect(*args, **kwargs):
            filename = args[0]
            if filename in self.file_data:
                return MagicMock(read=MagicMock(side_effect=[self.file_data[filename], b'']))
            else:
                return MagicMock(read=MagicMock(side_effect=[b'some data', b'']))

        self.mock_open.side_effect = side_effect

        # Execute
        hash_directory('/fake/dir')

        # Verify that hash was updated correctly
        calls = [call().update(data) for data in self.file_data.values()]
        mock_hash.assert_has_calls(calls, any_order=True)

    def test_empty_directory(self):
        # Test with an empty directory
        self.mock_walk.return_value = [('/fake/empty', (), ())]
        result = hash_directory('/fake/empty')
        self.assertEqual(result, hashlib.sha256(''.encode('utf-8')).hexdigest())

    def test_nonexistent_directory(self):
        # Test with a nonexistent directory
        self.mock_walk.return_value = []
        result = hash_directory('/fake/nonexistent')
        self.assertEqual(result, hashlib.sha256(''.encode('utf-8')).hexdigest())

    def test_file_read_error(self):
        # Test with a read error on one file
        self.file_data['/fake/dir/file1.txt'] = IOError("Cannot read file")
        self.mock_open.side_effect = IOError("Cannot read file")
        with self.assertRaises(IOError):
            hash_directory('/fake/dir')

    @patch('hashlib.sha256')
    def test_consistent_hash_order(self, mock_hash):
        # Ensure that hashing order does not affect the result
        mock_hash.return_value.hexdigest.return_value = 'consistenthash'
        hash1 = hash_directory('/fake/dir')
        self.fake_walk.reverse()  # Reverse the walk order
        hash2 = hash_directory('/fake/dir')
        self.assertEqual(hash1, hash2)
import os
import hashlib


def hash_directory(directory):
    """
    Compute a SHA-256 hash of all files within a given directory recursively.

    Args:
    directory (str): Path to the directory whose contents should be hashed.

    Returns:
    str: A SHA-256 hash of the directory's contents.
    """
    file_hashes = []
    for root, dirs, files in os.walk(directory):
        for file in sorted(files):  # Sort files to ensure consistent order
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    sha256_hash = hashlib.sha256()
                    for byte_block in iter(lambda: f.read(4096), b""):
                        sha256_hash.update(byte_block)
                    file_hashes.append(sha256_hash.hexdigest())
            except IOError as e:
                print(f"Error reading {file_path}: {e}")

    # Sort the list of file hashes before concatenation for consistency
    file_hashes.sort()
    concatenated_hashes = "".join(file_hashes)

    # Hash the concatenated string of all file hashes
    directory_hash = hashlib.sha256(concatenated_hashes.encode('utf-8')).hexdigest()
    return directory_hash
