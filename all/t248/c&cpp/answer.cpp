#include <iostream>
#include <map>
#include <vector>
#include <string>

std::map<std::string, std::string> sanitizeData(const std::map<std::string, std::string>& data, const std::vector<std::string>& keyToRemove = {}) {
    std::map<std::string, std::string> sanitizedData;
    for (const auto& pair : data) {
        if (std::find(keyToRemove.begin(), keyToRemove.end(), pair.first) == keyToRemove.end()) {
            sanitizedData[pair.first] = pair.second;
        }
    }
    return sanitizedData;
}