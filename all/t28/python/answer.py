def print_memory_bits(memory_section: bytes):
    """
    Prints the status of each bit (0 or 1) in the given section of memory.print format eg: Byte 0: 1 1 0 0 1 1 0 0 \nByte 1: 1 1 1 1 0 0 0 0

    :param memory_section: A bytes object representing the section of memory to be read.
    """
    for byte_index, byte in enumerate(memory_section):
        print(f"{byte_index}", end="")
        for bit_index in range(8):
            # Shift the bit to the right and check the least significant bit
            bit_status = (byte >> (7 - bit_index)) & 1
            print(bit_status, end=" ")
        print()  # Newline after each byte
