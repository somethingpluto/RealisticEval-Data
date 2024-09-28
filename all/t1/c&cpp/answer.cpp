#include <iostream>
#include <variant>
#include <string>
#include <sstream>

std::variant<int, double, std::string> numerical_str_convert(const std::string &value) {
    // Attempt to convert the string to an integer
    try {
        // Try to convert to integer
        std::size_t pos;
        int intValue = std::stoi(value, &pos);
        if (pos == value.size()) {
            return intValue;
        }
    } catch (const std::invalid_argument& e) {
        // Not an integer, continue to next conversion
    } catch (const std::out_of_range& e) {
        // Integer value out of range, continue to next conversion
    }
    
    // Attempt to convert the string to a floating point number
    try {
        // Try to convert to double
        std::size_t pos;
        double doubleValue = std::stod(value, &pos);
        if (pos == value.size()) {
            return doubleValue;
        }
    } catch (const std::invalid_argument& e) {
        // Not a floating point number, continue to next conversion
    } catch (const std::out_of_range& e) {
        // Double value out of range, continue to next conversion
    }
    
    // If neither integer nor floating point number, return original string
    return value;
}