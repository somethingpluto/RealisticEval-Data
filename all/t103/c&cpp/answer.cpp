#include <string>

std::string truncateStringWithReplacement(const std::string& str, size_t maxLength) {
    // Check if the string length is less than or equal to the specified length
    if (str.length() <= maxLength) {
        return str; // No need to truncate
    }

    // Replace the excess part with ellipsis
    return str.substr(0, maxLength) + "...";
}