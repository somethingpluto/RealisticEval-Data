#include <iostream>
#include <regex>
#include <string>

bool validURL(const std::string& str) {
    // Simplified and robust regex for URL validation
    const std::regex pattern(R"(^((http|https):\/\/)?"
        R"((([a-zA-Z\d]([a-zA-Z\d-]*[a-zA-Z\d])*)\.)+[a-zA-Z]{2,}|"
        R"((\d{1,3}\.){3}\d{1,3})"
        R"(:\d+)?"
        R"((\/[-a-zA-Z\d%_.~+]*)*)"
        R"((\?[;&a-zA-Z\d%_.~+=-]*)?)"
        R"((\#[-a-zA-Z\d_]*)?)$)");

    return std::regex_match(str, pattern);
}