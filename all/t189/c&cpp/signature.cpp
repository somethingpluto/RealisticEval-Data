/**
 * @brief Encodes a byte array into a Base64 encoded string.
 *
 * This function takes a vector of unsigned char data as input and converts it
 * into a Base64 encoded string.
 *
 * @param data A vector of unsigned char representing the input data to be encoded.
 * @return A std::string containing the Base64 encoded representation of the input data.
 *
 */
std::string base64_encode(const std::vector<unsigned char>& data);