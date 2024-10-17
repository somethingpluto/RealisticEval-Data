#include <iostream>
#include <map>
#include <string>
#include <cctype>

// Function to check if a string is numeric with possible comma and negative sign
bool isNumeric(const std::string& value) {
    std::string temp = value;
    size_t count = 0;
    for (char& c : temp) {
        if (c == ',') {
            if (++count > 1) return false; // More than one comma is invalid
            c = '.'; // Replace comma with dot
        } else if (c == '-') {
            if (&c != &temp[0]) return false; // Negative sign must be at the beginning
            c = '0'; // Replace negative sign temporarily
        }
    }
    return std::all_of(temp.begin(), temp.end(), ::isdigit);
}

// Function to convert numeric values in a CSV row from string format to a standardized format
std::map<std::string, std::string> convertCsvValues(const std::map<std::string, std::string>& row) {
    std::map<std::string, std::string> convertedRow;

    for (const auto& item : row) {
        const std::string& key = item.first;
        const std::string& value = item.second;

        if (isNumeric(value)) {
            std::string newValue = value;
            for (char& c : newValue) {
                if (c == ',') {
                    c = '.'; // Replace comma with dot
                }
            }
            convertedRow[key] = newValue;
        } else {
            convertedRow[key] = ""; // Use empty string to represent None
        }
    }

    return convertedRow;
}