#include <iostream>
#include <string>
#include <cmath>
#include <sstream>

std::string setEurValue(const std::string& value) {
    // Check for empty input
    if (value.empty()) return "";

    // Attempt to parse the input value to an integer
    try {
        long long number = std::stoll(value);
        
        // Determine the suffix and division based on the size of the number
        if (number >= 1'000'000) {
            std::ostringstream oss;
            oss << std::fixed << std::setprecision(1) << (number / 1'000'000.0) << 'm';
            return oss.str();  // Format for millions
        } else if (number >= 1'000) {
            std::ostringstream oss;
            oss << std::fixed << std::setprecision(1) << (number / 1'000.0) << 'k';
            return oss.str();  // Format for thousands
        } else {
            return std::to_string(number);  // Return as string for smaller numbers
        }
    } catch (...) {
        return "";  // Return empty string for non-numeric inputs
    }
}