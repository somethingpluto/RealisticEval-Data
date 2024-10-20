/**
 * @brief Converts a byte array into its corresponding hexadecimal string representation.
 *
 * @param byte_array The array of bytes to be converted into a hexadecimal string.
 *                   Must be a non-empty vector of unsigned char.
 * @type byte_array const std::vector<unsigned char>&
 *
 * @return A string representing the hexadecimal values of the bytes in the input array. 
 *         Returns an empty string if the input array is empty.
 * @rtype std::string
 */

std::string byte_array_to_hex_string(const std::vector<unsigned char>& byte_array);