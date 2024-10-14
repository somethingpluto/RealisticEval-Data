#include <iostream>
#include <regex>
#include <string>

std::string convertTime(const std::string& duration) {
    std::regex regex(R"(PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)(\.\d+)?S)?)");
    std::smatch matches;

    if (!std::regex_match(duration, matches, regex)) return ""; // Return an empty string if the input doesn't match

    std::string convertedTime;
    if (matches[1].length() > 0) {
        convertedTime += matches[1].str() + "h";
    }
    if (matches[2].length() > 0) {
        convertedTime += matches[2].str() + "m";
    }
    if (matches[3].length() > 0) {
        convertedTime += matches[3].str() + "s";
    }
    if (matches[4].length() > 0) {
        int milliseconds = static_cast<int>(std::round(std::stod(matches[4].str()) * 1000));
        if (milliseconds > 0) {
            convertedTime += std::to_string(milliseconds) + "ms";
        }
    }

    return convertedTime;
}