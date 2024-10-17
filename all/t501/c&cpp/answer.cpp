#include <iostream>
#include <string>
#include <sstream>

// Function to convert a string concatenated with underscores to a short format
std::string convert_to_short_format(const std::string& input_str) {
    std::istringstream iss(input_str);
    std::string segment;
    std::string short_format;

    // Split the input string by underscores and extract the first character from each segment
    while (std::getline(iss, segment, '_')) {
        if (!segment.empty()) {
            short_format += segment[0];
        }
    }

    return short_format;
}
