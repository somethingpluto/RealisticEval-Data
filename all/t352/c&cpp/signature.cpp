/**
 * @brief Converts a hexadecimal string into a byte array.
 *
 * @param hex_str The hexadecimal string to be converted. 
 *                This string should only contain hexadecimal characters (0-9, A-F, a-f). 
 *                If the string has an odd number of characters, a leading zero is added 
 *                to ensure proper conversion.
 * @type hex_str std::string
 *
 * @return A byte array representing the binary data encoded in the hex string.
 * @rtype std::vector<uint8_t>
 */

std::vector<uint8_t> hex_string_to_byte_array(const std::string& hex_str);