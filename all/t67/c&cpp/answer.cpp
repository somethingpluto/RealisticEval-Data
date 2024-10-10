#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <string>

std::map<std::string, std::string> parseXamlToDict(const std::string& xamlFile) {
    std::map<std::string, std::string> result;
    std::ifstream file(xamlFile);

    if (!file.is_open()) {
        std::cerr << "Failed to open file: " << xamlFile << std::endl;
        return result;
    }

    std::string line;
    while (getline(file, line)) {
        size_t start = line.find("<String key=\"");
        if (start != std::string::npos) {
            // Find the end of the key attribute
            size_t endKey = line.find("\"", start + 10);
            if (endKey != std::string::npos) {
                std::string key = line.substr(start + 10, endKey - start - 10);

                // Find the end of the String element
                size_t endElement = line.find("</String>");
                if (endElement != std::string::npos) {
                    std::string value = line.substr(endKey + 2, endElement - endKey - 2);
                    result[key] = value;
                }
            }
        }
    }

    file.close();
    return result;
}