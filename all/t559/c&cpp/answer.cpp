#include <string>
#include <regex>

bool isCppHeaderFile(const std::string& fileName) {
    // Define a regular expression to match C++ header file extensions
    std::regex cppHeaderExtensions(R"(\.(h|hh|hpp|hxx)$)", std::regex_constants::icase);

    // Test the file name against the regular expression
    return std::regex_search(fileName, cppHeaderExtensions);
}