#include <string>
#include <regex>

int getLineNumber(const std::string& content, size_t index) {
    // Ensure the index is within the bounds of the string
    if (index > content.length()) {
        throw std::out_of_range("Index is out of bounds");
    }

    // Count the number of newline characters in the substring
    std::string substring = content.substr(0, index);
    size_t lineCount = std::count(substring.begin(), substring.end(), '\n');

    return lineCount + 1; // Return the line number (1-based)
}