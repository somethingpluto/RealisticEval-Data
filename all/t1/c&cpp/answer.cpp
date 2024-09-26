#include <string>
#include <variant>
#include <stdexcept>
#include <sstream>

/**
 * @brief Convert a string representation of a number to an integer, float, or return the original string.
 *
 * This function attempts to parse the input string as an integer first. If the parsing fails, it then tries
 * to parse it as a floating-point number. If both conversions fail, the original string is returned.
 *
 * @param value The input string to be converted.
 * @return std::variant<int, double, std::string> The converted integer or float, or the original string.
 */
std::variant<int, double, std::string> numericalStrConvert(const std::string& value) {
    // Attempt to convert to integer
    try {
        size_t idx;
        int intValue = std::stoi(value, &idx);
        // Check if the whole string was consumed
        if (idx == value.length()) {
            return intValue;  // Return as integer if it matches original string
        }
    } catch (const std::invalid_argument&) {
        // Not a valid integer
    } catch (const std::out_of_range&) {
        // Integer out of range
    }

    // If not an integer, attempt to convert to float
    try {
        size_t idx;
        double floatValue = std::stod(value, &idx);
        // Check if the whole string was consumed
        if (idx == value.length()) {
            return floatValue;  // Return as float if it matches original string
        }
    } catch (const std::invalid_argument&) {
        // Not a valid float
    } catch (const std::out_of_range&) {
        // Float out of range
    }

    // If neither, return the original string
    return value;
}
