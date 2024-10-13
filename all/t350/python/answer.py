def byte_array_to_hex_string(byte_array):
    hex_string = ''.join([f"{b:02X}" for b in byte_array])
    return hex_string