#include <iostream>
#include <string>
#include <map>

std::string safe_format(const std::string& templateStr, const std::map<std::string, std::string>& kwargs) {
    std::string result = templateStr;
    size_t pos = 0;

    while ((pos = result.find("{", pos)) != std::string::npos) {
        size_t endPos = result.find("}", pos);
        if (endPos == std::string::npos)
            break; // No closing brace found

        std::string key = result.substr(pos + 1, endPos - pos - 1);
        auto it = kwargs.find(key);
        if (it != kwargs.end()) {
            result.replace(pos, endPos - pos + 1, it->second);
        }
        pos = endPos + 1;
    }

    return result;
}