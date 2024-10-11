#include <iostream>
#include <string>
#include <sstream>
#include <vector>

bool isCompliantIP(const std::string& ip) {
    // Split the IP address by '.'
    std::istringstream iss(ip);
    std::vector<int> parts;
    std::string part;

    while (std::getline(iss, part, '.')) {
        if (part.empty()) return false;  // Empty segment

        // Convert part to integer
        int num = std::stoi(part);

        // Check if the number is within the valid range [0, 255]
        if (num < 0 || num > 255) return false;

        parts.push_back(num);
    }

    // There should be exactly four segments
    if (parts.size() != 4) return false;

    return true;
}