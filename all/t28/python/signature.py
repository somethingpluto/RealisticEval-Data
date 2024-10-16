def print_memory_bits(memory_section: bytes):
    """
    Prints the status of each bit (0 or 1) in the given section of memory.
    For example:
        input: 0b10101010
        output: 10101010
    If have multiple bytes use \n split
    For example:
        input: [0b11001100, 0b11110000]
        output: 11001100\n11110000

    Args:
        memory_section (bytes): A bytes object representing the section of memory to be read.

    Returns:

    """
