/**
 * @brief Extracts the position and bits of a specific character from a byte array.
 *
 * @param byte_array The byte array to search within
 * @param char The character to find in the byte array
 * @param charset The character encoding of the byte array
 * @return A pair of (position, bits) if the character is found, otherwise an empty pair.
 */
std::pair<int, std::string> extract_character_bits(const std::vector<unsigned char>& byteArray, const std::string& charStr, const std::string& charset = "utf-8") {}