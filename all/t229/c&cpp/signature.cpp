/**
 * Converts a file size in bytes to a human-readable format.
 * For example:
 *     input: 2120
 *     output: 2KB
 *
 * @param size_bytes The size in bytes to be converted.
 * @return A string representing the converted size in a human-readable format (e.g., "2KB", "1MB").
 */
std::string convertFileSize(int64_t sizeBytes);