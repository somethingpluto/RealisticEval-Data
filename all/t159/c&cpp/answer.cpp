#include <string>

std::string removeFileExtension(const std::string& file_name) {
    // Find the index of the last dot in the file name
    size_t lastDotIndex = file_name.find_last_of('.');

    // If a dot is found and it is not the first character
    if (lastDotIndex != std::string::npos && lastDotIndex != 0) {
        // Return the substring from the beginning to the last dot
        return file_name.substr(0, lastDotIndex);
    }

    // Return the original file name if no dot is found
    return file_name;
}