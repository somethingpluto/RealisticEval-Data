#include <iostream>
#include <regex>
#include <string>
#include <vector>

std::vector<std::string> findPlaceholders(const std::string& text) {
    std::regex pattern(R"(\{\{.*?\}\})");
    std::sregex_iterator iter(text.begin(), text.end(), pattern);
    std::sregex_iterator end;
    
    std::vector<std::string> result;
    while(iter != end) {
        result.push_back((*iter)[0].str());
        ++iter;
    }
    
    return result;
}