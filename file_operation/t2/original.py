# Script created by ChatGPT to dump memory from the GameOfLife gameboard into a human readable text format.
# To dump memory, save memory $0300 to $0420 into a file then run this script on that file
import argparse

def read_bits(file_path, width):
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

            # Add a final newline for formatting, if needed
            if bit_count != 0:
                print()

    except IOError:
        print("Error: File not found or cannot be read.")

def main():
    parser = argparse.ArgumentParser(description='Read a file bit by bit.')
    parser.add_argument('file_path', type=str, help='Path to the file')
    parser.add_argument('width', type=int, help='Number of bits per line')

    args = parser.parse_args()
    read_bits(args.file_path, args.width)

if __name__ == '__main__':
    main()