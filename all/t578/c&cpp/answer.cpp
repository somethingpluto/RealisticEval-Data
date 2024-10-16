#include <iostream>
#include <regex>
#include <string>

bool isKebabCase(const std::string& input) {
    // Regular expression to match KEBAB_CASE
    std::regex kebabCaseRegex("^[a-z]+(-[a-z]+)*$");
    return std::regex_match(input, kebabCaseRegex);
}

int main() {
    std::string input = "example-string";
    std::cout << std::boolalpha << isKebabCase(input) << std::endl; // Outputs: true
    return 0;
}