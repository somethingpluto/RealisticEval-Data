import hashlib
import os


def hash_directory(directory): # Written by Chatgpt...
    file_hashes = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                sha256_hash = hashlib.sha256()
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)

                file_hashes.append(sha256_hash.hexdigest())

    # Concatenate individual file hashes and hash the model_answer_result
    directory_hash = hashlib.sha256("".join(file_hashes).encode()).hexdigest()
    return directory_hash
