#include <string>
#include <regex>

std::string getFileExtension(const std::string& file_name) {
    std::regex regex(R"((?:\.([^.]+))?$)");
    std::smatch match;

    if (std::regex_search(file_name, match, regex) && match.size() > 1) {
        return match[1].str();
    }

    return "";
}