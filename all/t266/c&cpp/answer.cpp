#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <typeinfo>
#include <stdexcept>

// Function to handle nested data
std::variant<std::map<std::string, std::variant<int, double, std::string>>, std::vector<std::variant<int, double, std::string>>, std::string, int, double> handle_nested_data(const std::variant<std::map<std::string, std::variant<int, double, std::string>>, std::vector<std::variant<int, double, std::string>>, std::string, int, double>& data) {
    using VarType = std::variant<std::map<std::string, std::variant<int, double, std::string>>, std::vector<std::variant<int, double, std::string>>, std::string, int, double>;

    if (std::holds_alternative<std::map<std::string, VarType>>(data)) {
        auto mapData = std::get<std::map<std::string, VarType>>(data);
        std::map<std::string, VarType> result;
        for (const auto& pair : mapData) {
            result[pair.first] = handle_nested_data(pair.second);
        }
        return result;
    } else if (std::holds_alternative<std::vector<VarType>>(data)) {
        auto vecData = std::get<std::vector<VarType>>(data);
        std::vector<VarType> result;
        for (const auto& item : vecData) {
            result.push_back(handle_nested_data(item));
        }
        return result;
    } else if (std::holds_alternative<std::string>(data)) {
        auto strData = std::get<std::string>(data);
        try {
            return std::stoi(strData);
        } catch (const std::invalid_argument&) {
            try {
                return std::stod(strData);
            } catch (const std::invalid_argument&) {
                return strData; // Return the original string if it's not a number
            }
        }
    } else if (std::holds_alternative<int>(data)) {
        return std::get<int>(data);
    } else if (std::holds_alternative<double>(data)) {
        return std::get<double>(data);
    }

    throw std::runtime_error("Unsupported data type");
}