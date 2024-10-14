#include <string>
#include <regex>
#include <algorithm>

std::string compressHTML(const std::string& html) {
    std::string result = html;
    // Remove leading/trailing whitespace around tags
    result = std::regex_replace(result, std::regex("\\s*(<[^>]+>)\\s*"), "$1");
    // Remove multiple newlines and replace with a single space
    result = std::regex_replace(result, std::regex("\n+"), " ");
    // Remove multiple spaces and replace them with a single space
    result = std::regex_replace(result, std::regex("[ \t]+"), " ");
    // Trim whitespace from both ends
    result.erase(result.begin(), std::find_if(result.begin(), result.end(), [](unsigned char ch) {
        return !std::isspace(ch);
    }));
    result.erase(std::find_if(result.rbegin(), result.rend(), [](unsigned char ch) {
        return !std::isspace(ch);
    }).base(), result.end());
    return result;
}