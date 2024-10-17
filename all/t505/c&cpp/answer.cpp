#include <iostream>
#include <regex>
#include <string>

std::string camel_to_snake(const std::string& camel_str) {
    /**
     * Convert a CamelCase string to snake_case.
     *
     * Parameters:
     * camel_str (const std::string&): The CamelCase string to convert.
     *
     * Returns:
     * std::string: The converted snake_case string.
     */
    std::string snake_case_str;
    std::regex reg("(.)([A-Z][a-z]+)");
    std::regex reg2("([a-z0-9])([A-Z])");

    // Insert underscores before each uppercase letter and convert to lowercase
    snake_case_str = std::regex_replace(camel_str, reg, "$1_$2");
    snake_case_str = std::regex_replace(snake_case_str, reg2, "$1_$2");

    // Convert the entire string to lowercase
    std::transform(snake_case_str.begin(), snake_case_str.end(), snake_case_str.begin(), ::tolower);

    return snake_case_str;
}
