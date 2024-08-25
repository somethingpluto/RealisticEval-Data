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
