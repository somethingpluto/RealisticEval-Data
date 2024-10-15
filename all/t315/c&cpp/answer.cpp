#include <iostream>
#include <string>
#include <sstream>
#include <unordered_map>
#include <stdexcept>
#include <iomanip>

std::string decodeURIComponent(const std::string& encoded) {
    std::string decoded;
    for (size_t i = 0; i < encoded.length(); i++) {
        if (encoded[i] == '%') {
            int value;
            std::stringstream ss;
            ss << std::hex << encoded.substr(i + 1, 2);
            ss >> value;
            decoded += static_cast<char>(value);
            i += 2; // Skip the next two characters
        } else {
            decoded += encoded[i];
        }
    }
    return decoded;
}

std::string getFileIdFromUrl(const std::string& url) {
    try {
        size_t queryStart = url.find('?');
        if (queryStart == std::string::npos) {
            return ""; // No query parameters
        }

        std::string query = url.substr(queryStart + 1);
        std::unordered_map<std::string, std::string> params;

        // Parse the query parameters
        std::istringstream iss(query);
        std::string pair;
        while (std::getline(iss, pair, '&')) {
            size_t pos = pair.find('=');
            if (pos != std::string::npos) {
                std::string key = pair.substr(0, pos);
                std::string value = pair.substr(pos + 1);
                params[key] = value;
            }
        }

        // Extract the file ID using 'fileId' as the key
        auto it = params.find("fileId");
        if (it != params.end()) {
            return decodeURIComponent(it->second);
        }
        return ""; // Return empty string if 'fileId' is not found
    } catch (const std::exception& e) {
        std::cerr << "Invalid URL: " << e.what() << std::endl;
        return ""; // Return empty string if an error occurs
    }
}