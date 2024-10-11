#include <iostream>
#include <string>
#include <sstream>
#include <variant>

std::variant<int, float, std::string> numericalStrConvert(const std::string& value) {
    // Try to convert to an integer
    try {
        size_t idx;
        int intValue = std::stoi(value, &idx);
        // Ensure the entire string was consumed
        if (idx == value.length()) {
            return intValue;
        }
    } catch (const std::invalid_argument&) {
        // Not an integer
    } catch (const std::out_of_range&) {
        // Integer out of range
    }

    // Try to convert to a float
    try {
        size_t idx;
        float floatValue = std::stof(value, &idx);
        // Ensure the entire string was consumed
        if (idx == value.length()) {
            return floatValue;
        }
    } catch (const std::invalid_argument&) {
        // Not a float
    } catch (const std::out_of_range&) {
        // Float out of range
    }

    // Return the original string if neither conversion succeeded
    return value;
}