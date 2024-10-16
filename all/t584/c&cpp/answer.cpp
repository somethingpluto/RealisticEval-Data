#include <string>
#include <regex>

bool isPascalCase(const std::string& input) {
    std::regex pascalCaseRegex("^[A-Z][a-z]*(?:[A-Z][a-z]*)*$");
    return std::regex_match(input, pascalCaseRegex);
}