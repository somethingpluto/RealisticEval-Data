#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>

bool isValidUsername(const std::string& username) {
    // Check if the input is empty
    if (username.empty()) {
        return false; // Return false if the input is empty
    }

    // Trim leading and trailing whitespace
    std::string trimmedUsername = username;
    trimmedUsername.erase(trimmedUsername.begin(), std::find_if(trimmedUsername.begin(), trimmedUsername.end(), [](unsigned char ch) {
        return !std::isspace(ch);
    }));
    trimmedUsername.erase(std::find_if(trimmedUsername.rbegin(), trimmedUsername.rend(), [](unsigned char ch) {
        return !std::isspace(ch);
    }).base(), trimmedUsername.end());

    // Check the length of the username
    size_t length = trimmedUsername.length();
    if (length < 5 || length > 16) {
        return false; // Return false if length is not within the valid range
    }

    // Check if the username contains only alphanumeric characters and spaces
    for (char ch : trimmedUsername) {
        if (!std::isalnum(ch) && !std::isspace(ch)) {
            return false; // Return false if a character is invalid
        }
    }

    return true; // Return true if valid
}

int main() {
    std::string username;
    std::cout << "Enter username: ";
    std::getline(std::cin, username);

    if (isValidUsername(username)) {
        std::cout << "Valid username!" << std::endl;
    } else {
        std::cout << "Invalid username!" << std::endl;
    }

    return 0;
}