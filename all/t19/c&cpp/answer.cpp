#include <iostream>
#include <regex>
#include <string>

bool contains_phone_number(const std::string& s) {
    std::regex pattern(R"((\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4}))");
    return std::regex_search(s, pattern);
}