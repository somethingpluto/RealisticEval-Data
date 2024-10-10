#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

std::string replaceWordsInFile(const std::string& filePath, const std::map<std::string, std::string>& replacementDict) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        throw std::runtime_error("Unable to open file");
    }

    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string content = buffer.str();

    for (const auto& pair : replacementDict) {
        size_t pos = 0;
        while ((pos = content.find(pair.first, pos)) != std::string::npos) {
            content.replace(pos, pair.first.length(), pair.second);
            pos += pair.second.length();
        }
    }

    file.close();
    return content;
}