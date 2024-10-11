#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm> // for std::remove_if


void splitComma(const std::string& str, std::vector<std::string>& vect) {
    std::stringstream ss(str);
    std::string token;

    // Clear the output vector to avoid residual data
    vect.clear();

    // Process each comma-separated token
    while (std::getline(ss, token, ',')) {
        // Trim leading and trailing whitespace
        token.erase(token.begin(), std::find_if(token.begin(), token.end(), [](unsigned char c) {
            return !std::isspace(c);
        }));
        token.erase(std::find_if(token.rbegin(), token.rend(), [](unsigned char c) {
            return !std::isspace(c);
        }).base(), token.end());

        // Only add non-empty tokens to the vector
        if (!token.empty()) {
            vect.push_back(token);
        }
    }
}
