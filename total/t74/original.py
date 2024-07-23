# Written by chatGPT

import struct

def decimal_to_binary(decimal_num, num_bits):
    if num_bits == 32:
        # Convert decimal number to 32-bit binary representation
        binary_num = struct.pack('>f', decimal_num)
        binary_num = struct.unpack('>l', binary_num)[0]
        binary_num = bin(binary_num & 0xffffffff)[2:].zfill(32)
    elif num_bits == 64:
        # Convert decimal number to 64-bit binary representation
        binary_num = struct.pack('>d', decimal_num)
        binary_num = struct.unpack('>q', binary_num)[0]
        binary_num = bin(binary_num & 0xffffffffffffffff)[2:].zfill(64)
    else:
        return "Invalid number of bits. Please specify either 32 or 64."

    return binary_num


if __name__ == '__main__':
    decimal_num = eval(input("decimal_num: "))
    num_bits = int(input("num_bits: "))
    print("result:",decimal_to_binary(decimal_num, num_bits))