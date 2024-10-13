import hashlib
import os


def hash_password_with_salt(password: str) -> bytes:
    """
    Generates a 16-byte random salt value, hashes the provided password with that salt
    using the SHA-256 hash algorithm, and returns the combined salt and hashed password.

    :param password: The password to be hashed.
    :return: A byte array containing the salt followed by the hashed password.
    """
    # Generate a 16-byte random salt
    salt = generate_random_salt(16)
    # Hash the password with the salt using SHA-256
    hashed_password = hash_with_sha256(password, salt)
    # Combine the salt and the hashed password
    salt_and_hashed_password = salt + hashed_password
    return salt_and_hashed_password


def generate_random_salt(length: int) -> bytes:
    """
    Generates a random salt of the specified length.

    :param length: The length of the salt in bytes.
    :return: A byte array containing the generated salt.
    """
    return os.urandom(length)


def hash_with_sha256(password: str, salt: bytes) -> bytes:
    """
    Hashes the provided password with the given salt using the SHA-256 hash algorithm.

    :param password: The password to be hashed.
    :param salt: The salt to be used in the hashing process.
    :return: A byte array containing the hashed password.
    """
    # Create a new sha256 hash object
    hasher = hashlib.sha256()
    # Update the hash object with the salt
    hasher.update(salt)
    # Hash the password
    hasher.update(password.encode('utf-8'))
    # Return the hashed password
    return hasher.digest()
