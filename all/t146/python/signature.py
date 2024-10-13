def format_bytes(bytes: int, options: dict = None) -> str:
    """
    Formats a given number of bytes into a human-readable string representation,
    using either the SI (decimal) or binary (accurate) size notation.

    :param bytes: The number of bytes to format.
    :param options: Optional settings to customize the output.
    :param options['decimals']: Number of decimal places to include in the result.
    :param options['sizeType']: Specifies whether to use binary ("accurate") or 
        decimal ("normal") units.
        "accurate" uses units like KiB, MiB (base 1024).
        "normal" uses units like KB, MB (base 1000).
    :returns: A string representation of the byte size in a human-readable format.
    """