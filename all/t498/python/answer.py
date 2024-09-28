import hashlib


def compute_md5(input_string):
    """
    Computes and returns the MD5 hash of the input string.

    :param input_string: The string to be hashed
    :return: The MD5 hash of the input string in hexadecimal format
    """
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes of the input string
    md5_hash.update(input_string.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()