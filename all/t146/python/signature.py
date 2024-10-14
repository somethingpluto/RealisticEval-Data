def format_bytes(bytes: int, options: dict = None) -> str:
    """
    Formats a given number of bytes into a human-readable string representation,
    using either the SI (decimal) or binary (accurate) size notation.

    Args:
        bytes (int): The number of bytes to format.
        options (dict, optional): Optional settings to customize the output.
            - 'decimals' (int): Number of decimal places to include in the result.
            - 'sizeType' (str): Specifies whether to use binary ("accurate") or
              decimal ("normal") units.
              "accurate" uses units like KiB, MiB (base 1024).
              "normal" uses units like KB, MB (base 1000).

    Returns:
        str: A string representation of the byte size in a human-readable format.
    """
