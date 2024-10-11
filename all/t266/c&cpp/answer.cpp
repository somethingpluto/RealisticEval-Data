#include <iostream>
#include <map>
#include <string>
#include <variant>

// Define a variant type to represent different types of values in the dictionary
using Value = std::variant<std::string, int, double, std::map<std::string, Value>>;

class NestedDataHandler {
public:
    // Function to handle nested data
    static Value handleNestedData(const Value& data) {
        return std::visit(handleVisitor{}, data);
    }

private:
    // Visitor class to handle different variants
    struct HandleVisitor {
        Value operator()(const std::string& str) const {
            // Decode bytes to UTF-8 strings (assuming already decoded)
            return str;
        }

        Value operator()(int num) const {
            // Convert numbers to integers
            return num;
        }

        Value operator()(double num) const {
            // Convert numbers to floating point numbers
            return num;
        }

        Value operator()(const std::map<std::string, Value>& dict) const {
            // Recursively handle nested dictionaries
            std::map<std::string, Value> result;
            for (const auto& [key, value] : dict) {
                result[key] = handleNestedData(value);
            }
            return result;
        }
    };

    static HandleVisitor handleVisitor;
};
