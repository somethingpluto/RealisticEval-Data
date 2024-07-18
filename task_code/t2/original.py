def read_and_print_bits(file_path, width):
    try:
        with open(file_path, "rb") as file:
            byte = file.read(1)
            bit_count = 0
            while byte:
                bits = f'{int.from_bytes(byte, "big"):08b}'
                for bit in bits:
                    print(bit, end='')
                    bit_count += 1
                    if bit_count == width:
                        print('\n', end='')
                        bit_count = 0
                byte = file.read(1)
            if bit_count != 0:
                print()

    except IOError:
        print("Error: File not found or cannot be read.")