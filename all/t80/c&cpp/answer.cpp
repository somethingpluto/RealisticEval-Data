#include <iostream>
#include <string>
#include <regex>

// Function to remove illegal characters from Windows file path string
std::string sanitize_filename(const std::string& filename) {
    // Define the illegal characters for Windows filenames
    std::regex illegal_chars_pattern("[<>:\"/\\\\|?*\\x00-\\x1F]");

    // Replace illegal characters with an underscore
    std::string sanitized = std::regex_replace(filename, illegal_chars_pattern, "_");

    // Optionally, limit the length of the filename
    // Windows has a maximum path length of 260 characters
    const size_t max_length = 255;
    if (sanitized.length() > max_length) {
        sanitized = sanitized.substr(0, max_length);
    }

    return sanitized;
}