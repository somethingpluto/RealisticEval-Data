#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <vector>
#include <cctype>
#include <iomanip>

std::string encodeURIComponent(const std::string& str) {
    std::ostringstream encoded;
    for (unsigned char c : str) {
        if (isalnum(c) || c == '-' || c == '_' || c == '.' || c == '~') {
            encoded << c;
        } else {
            encoded << '%' << std::uppercase << std::hex << static_cast<int>(c);
        }
    }
    return encoded.str();
}

std::string toQueryString(const std::map<std::string, std::string>& params) {
    std::vector<std::string> queryParts;

    for (const auto& pair : params) {
        const std::string& key = pair.first;
        const std::string& value = pair.second;

        // Check for null/undefined values (in C++, we can check if the value is empty)
        if (!value.empty()) {
            // Encode the key and value, then add to the array
            queryParts.push_back(encodeURIComponent(key) + "=" + encodeURIComponent(value));
        }
    }

    if (!queryParts.empty()) {
        std::ostringstream queryString;
        queryString << "?" << queryParts[0];
        for (size_t i = 1; i < queryParts.size(); ++i) {
            queryString << "&" << queryParts[i];
        }
        return queryString.str();
    }

    return "";
}

int main() {
    std::map<std::string, std::string> params = {
        {"name", "John Doe"},
        {"age", "30"},
        {"city", "New York"},
        {"empty", ""}
    };

    std::string queryString = toQueryString(params);
    std::cout << queryString << std::endl; // Output: ?name=John%20Doe&age=30&city=New%20York

    return 0;
}