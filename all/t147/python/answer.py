def array_buffer_to_string(buffer: bytes) -> str:
    """
    Converts a bytes object to a string using UTF-8 decoding.

    :param buffer: A bytes object representing the data to convert.
    :returns: The decoded string.
    """
    return buffer.decode('utf-8')