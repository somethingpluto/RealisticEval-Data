#include <string>

/**
 * @brief Extracts the last part of a complete file path with the help of a separator and returns it, or the original string if no separator is found
 *
 * This function extracts the last part of a file path after the last occurrence of the specified separator.
 * If the separator is not found in the path, the function returns the original string.
 *
 * @param filePath The complete file path as a string.
 * @param separator The character used as a separator (e.g., '/' or '\\').
 * @return The last part of the file path after the last separator, or the original string if no separator is found.
 */
std::string getLastPartOfFilepath(const std::string& filePath, char separator) {
    size_t pos = filePath.find_last_of("/\\");
    if (pos == std::string::npos) {
        return filePath; // Return the original string if no separator is found
    }
    return filePath.substr(pos + 1);
}