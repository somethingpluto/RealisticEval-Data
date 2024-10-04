def print_memory_bits(memory_section: bytes):
    """
    Prints the status of each bit (0 or 1) in the given section of memory.

    Args:
        memory_section (bytes): A bytes object representing the section of memory to be read.

    Returns:

    """
    for byte in memory_section:
        print(' '.join(str((byte >> i) & 1) for i in range(7, -1, -1)))
