#include <iostream>
#include <sstream>
#include <vector>
#include <string>

std::vector<std::string> splitString(const std::string& str) {
    std::vector<std::string> result;
    std::istringstream iss(str);
    std::string word;

    while (iss >> word) {
        result.push_back(word);
    }

    return result;
}