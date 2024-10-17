#include <iostream>
#include <sstream>
#include <chrono>
#include <iomanip>

std::string format_date_string(const std::string& date_str) {
    /**
     * Converts a date string from the format '%a, %d %b %Y %H:%M:%S %z (%Z)'
     * to the format '%Y-%m-%d_%H:%M:%S'.
     *
     * Args:
     *     date_str (const std::string&): The input date string.
     *
     * Returns:
     *     std::string: The formatted date string in the format '%Y-%m-%d_%H:%M:%S'.
     *     Empty string: If the input date string is invalid.
     */

    std::istringstream iss(date_str);
    std::tm tm = {};
    std::string timezone;
    char dummy;

    // Attempt to parse the date string
    if (!(iss >> std::get_time(&tm, "%a, %d %b %Y %H:%M:%S %z") >> std::ws >> dummy >> std::ws >> timezone)) {
        std::cerr << "Error parsing date: Invalid format\n";
        return "";
    }

    // Convert to the desired output format
    std::ostringstream oss;
    oss << std::put_time(&tm, "%Y-%m-%d_%H:%M:%S");

    return oss.str();
}