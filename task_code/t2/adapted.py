def print_binary_from_file(file_path: str, line_width: int) -> None:
    """
    Read a binary file bit by bit and output the read bits line by line at a specified width (the number of bits per line)
    :param file_path: binary file path
    :param width: read bit width
    :return:
    """
    try:
        with open(file_path, "rb") as file:
            binary_string = ''.join(f'{byte:08b}' for byte in file.read())

        # Print formatted binary string
        for i in range(0, len(binary_string), line_width):
            print(binary_string[i:i + line_width])

    except IOError:
        print("Error: File not found or cannot be read.")
