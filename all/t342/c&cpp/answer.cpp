#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <unordered_map>

std::unordered_map<std::string, std::vector<std::string>> parseMarkdownTitles(const std::string& markdown) {
    std::unordered_map<std::string, std::vector<std::string>> result;
    result["level1"] = {};
    result["level2"] = {};
    result["level3"] = {};

    std::istringstream stream(markdown);
    std::string line;

    while (std::getline(stream, line)) {
        line.erase(0, line.find_first_not_of(" \n\r\t")); // Trim leading whitespace

        if (line.rfind("# ", 0) == 0) {
            result["level1"].push_back(line.substr(2)); // Remove '# ' prefix
        } else if (line.rfind("## ", 0) == 0) {
            result["level2"].push_back(line.substr(3)); // Remove '## ' prefix
        } else if (line.rfind("### ", 0) == 0) {
            result["level3"].push_back(line.substr(4)); // Remove '### ' prefix
        }
    }

    return result;
}
