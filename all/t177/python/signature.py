import hashlib
import os


def hash_password_with_salt(password: str) -> bytes:
    """
    Generates a 16-byte random salt value, hashes the provided password with that salt
    using the SHA-256 hash algorithm, and returns the combined salt and hashed password.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: A byte array containing the salt followed by the hashed password.
    """