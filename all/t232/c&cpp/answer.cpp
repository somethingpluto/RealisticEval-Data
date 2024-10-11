#include <iostream>
#include <string>
#include <regex>

int convert_hms_to_milliseconds(const std::string& timeStr) {
    std::smatch match;
    std::regex pattern("(\\d+)h(\\d+)min(\\d+)s");

    if (std::regex_search(timeStr, match, pattern)) {
        int hours = std::stoi(match[1]);
        int minutes = std::stoi(match[2]);
        int seconds = std::stoi(match[3]);

        return ((hours * 60 + minutes) * 60 + seconds) * 1000;
    } else {
        std::cerr << "Invalid input format." << std::endl;
        return -1; // Return an error code for invalid input
    }
}