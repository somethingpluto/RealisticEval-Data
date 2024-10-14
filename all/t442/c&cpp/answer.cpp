#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

// Helper function to check if a string contains a dot
bool containsDot(const std::string& str) {
    return str.find('.') != std::string::npos;
}

// Function to attempt conversion of a string to a number
template<typename T>
T stringToNumber(const std::string& str) {
    std::istringstream iss(str);
    T number;
    iss >> number;
    if (iss.fail() || !iss.eof()) {
        throw std::invalid_argument("Conversion failed");
    }
    return number;
}

// Main recursive function to convert strings to numbers
std::variant<std::string, int, double> convertStringsToNumbers(const std::variant<std::string, int, double, std::map<std::string, std::variant<std::string, int, double>>, std::vector<std::variant<std::string, int, double>>>& data) {
    if (std::holds_alternative<std::map<std::string, std::variant<std::string, int, double>>>(data)) {
        auto map = std::get<std::map<std::string, std::variant<std::string, int, double>>>(data);
        std::map<std::string, std::variant<std::string, int, double>> newMap;
        for (const auto& [key, value] : map) {
            newMap[key] = convertStringsToNumbers(value);
        }
        return newMap;
    } else if (std::holds_alternative<std::vector<std::variant<std::string, int, double>>>(data)) {
        auto vec = std::get<std::vector<std::variant<std::string, int, double>>>(data);
        std::vector<std::variant<std::string, int, double>> newVec;
        for (const auto& item : vec) {
            newVec.push_back(convertStringsToNumbers(item));
        }
        return newVec;
    } else if (std::holds_alternative<std::string>(data)) {
        std::string str = std::get<std::string>(data);
        try {
            if (containsDot(str)) {
                return stringToNumber<double>(str);
            } else {
                return stringToNumber<int>(str);
            }
        } catch (const std::invalid_argument&) {
            return str; // Return original string if conversion fails
        }
    } else {
        return data; // Return data unchanged if it's not a string
    }
}
