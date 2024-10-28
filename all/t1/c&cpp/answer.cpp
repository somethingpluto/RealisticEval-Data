#include <iostream>
#include <string>
#include <sstream>
#include <variant>

std::variant<int, float, std::string> numerical_str_convert(const std::string& value) {
    try {
        size_t idx;
        int intValue = std::stoi(value, &idx);
        // Ensure the entire string was consumed
        if (idx == value.length()) {
            return intValue;
        }
    } catch (const std::invalid_argument&) {
    } catch (const std::out_of_range&) {
    }

    try {
        size_t idx;
        float floatValue = std::stof(value, &idx);
        // Ensure the entire string was consumed
        if (idx == value.length()) {
            return floatValue;
        }
    } catch (const std::invalid_argument&) {
    } catch (const std::out_of_range&) {
    }

    return value;
}