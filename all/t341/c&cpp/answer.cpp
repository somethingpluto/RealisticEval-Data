#include <iostream>
#include <regex>
#include <stdexcept>
#include <string>

long long convertTimeHmsStringToMs(const std::string& str) {
    // Regular expression to parse the string for hours, minutes, and seconds
    std::regex regex(R"((?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?)");
    std::smatch match;

    // Throw an error if the string does not match the expected format
    if (!std::regex_match(str, match, regex)) {
        throw std::invalid_argument("Cannot convert hms string \"" + str + "\" to ms!");
    }

    // Parse hours, minutes, and seconds, defaulting to 0 if any group is missing
    int hours = match[1].length() ? std::stoi(match[1].str()) : 0;
    int minutes = match[2].length() ? std::stoi(match[2].str()) : 0;
    int seconds = match[3].length() ? std::stoi(match[3].str()) : 0;

    // Calculate the total milliseconds
    long long totalMilliseconds = ((hours * 60 + minutes) * 60 + seconds) * 1000;
    return totalMilliseconds;
}
