/**
 * @brief Extracts the last part of a complete file path with the help of a separator and returns it, or the original string if no separator is found
 *
 * @param filePath The complete file path as a string.
 * @return The last part of the file path after the last separator, or the original string if no separator is found.
 */
std::string getLastPartOfFilepath(const std::string& filePath) {
    std::string lastPart;
    std::vector<std::string> parts = split(filePath, '/');
    if (parts.empty()) {
        parts = split(filePath, '\\');
    }
    if (parts.empty()) {
        lastPart = filePath;
    } else {
        lastPart = parts.back();
    }
    return lastPart;
}
