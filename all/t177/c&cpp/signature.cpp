/**
 * @brief Generates a 16-byte random salt value, hashes the provided password with that salt
 *        using the SHA-256 hash algorithm, and returns the combined salt and hashed password.
 *
 * @param password The password to be hashed.
 *
 * @return A byte array containing the salt followed by the hashed password.
 */
std::vector<uint8_t> hash_password_with_salt(const std::string& password);