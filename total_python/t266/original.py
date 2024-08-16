from enum import Enum
from numbers import Number


def preprocess_data(data):
    """Generated with ChatGPT.

    Recursively process nested data: decode bytes to UTF-8 strings, convert numbers to integers or
    floats.
    """

    if isinstance(data, Enum):
        return data
    if isinstance(data, dict):
        # Recursively apply transformations to each key-value pair in the dictionary
        data = {preprocess_data(key): preprocess_data(value) for key, value in data.items()}
    if isinstance(data, list):
        # Apply transformations to each item in the list
        data = [preprocess_data(item) for item in data]
    if isinstance(data, bytes):
        data = data.strip(b"\x00")
        try:
            # Attempt to decode bytes to a UTF-8 string
            data = data.decode('utf-8')
        except UnicodeDecodeError:
            # Return hexadecimal representation if decoding fails
            data = data.hex()
    if isinstance(data, Number):
        try:
            # Attempt conversion to int if it matches exactly
            if data == int(data):
                data = int(data)
            else:
                data = float(data)
        except (ValueError, TypeError, OverflowError, NotImplementedError):
            # If conversion to int fails, fall back to float
            data = float(data)

    return data
