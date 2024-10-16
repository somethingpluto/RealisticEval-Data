#include <iostream>
#include <string>
#include <regex>
#include <chrono>

std::chrono::milliseconds genTimeoutTimedelta(const std::string &timeString) {
    std::regex pattern(R"((\d+)d\s*(\d+)h\s*(\d+)m\s*(\d+)s\s*(\d+)ms)");
    std::smatch match;
    if (!std::regex_search(timeString, match, pattern)) {
        throw std::invalid_argument("Invalid time format");
    }

    int days = std::stoi(match.str(1));
    int hours = std::stoi(match.str(2));
    int minutes = std::stoi(match.str(3));
    int seconds = std::stoi(match.str(4));
    int milliseconds = std::stoi(match.str(5));

    return std::chrono::hours(hours)
           + std::chrono::minutes(minutes)
           + std::chrono::seconds(seconds)
           + std::chrono::milliseconds(milliseconds)
           + std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::days(days));
}