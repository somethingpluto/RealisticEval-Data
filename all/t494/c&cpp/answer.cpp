#include <iostream>
#include <map>
#include <string>
#include <cctype>
#include <cmath>

// Function to check if a string contains only whitespace characters
bool is_whitespace(const std::string& str) {
    return str.find_first_not_of(" \t\n\v\f\r") == std::string::npos;
}

// Function to check if a floating-point number is NaN
bool is_nan(double value) {
    return std::isnan(value);
}

// Function to clean the input dictionary
std::map<std::string, std::string> clean_dictionary(const std::map<std::string, std::string>& input_dict) {
    std::map<std::string, std::string> cleaned_dict;

    for (const auto& item : input_dict) {
        const std::string& value = item.second;

        // Check if the value is not empty and not a whitespace string
        if (!value.empty() && !is_whitespace(value)) {
            // Since we are dealing with strings, no need to check for NaN
            cleaned_dict[item.first] = value;
        }
    }

    return cleaned_dict;
}