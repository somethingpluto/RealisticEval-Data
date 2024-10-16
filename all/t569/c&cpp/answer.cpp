#include <string>

std::string compressString(const std::string& input, size_t maxLength = 18) {
    // Check if the input string exceeds the maximum length
    if (input.length() > maxLength) {
        // Truncate the string to the maximum length minus 3 for the ellipsis
        return input.substr(0, maxLength - 3) + "..."; // Append ellipsis
    }
    return input; // Return the original string if it's within the length limit
}