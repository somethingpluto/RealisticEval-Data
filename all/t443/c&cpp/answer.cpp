#include <iostream>
#include <sstream>
#include <string>

std::string compress_whitespace(const std::string& input_string) {
    /**
     * Compress multiple consecutive whitespace characters in a string into a single space.
     *
     * Parameters:
     * input_string (const std::string&): The string to be processed.
     *
     * Returns:
     * std::string: The processed string with compressed whitespace.
     */

    std::istringstream iss(input_string);
    std::string token;
    std::string result;

    // Extract tokens separated by whitespace and join them with a single space
    while (iss >> token) {
        if (!result.empty()) {
            result += " ";
        }
        result += token;
    }

    return result;
}
