#include <iostream>
#include <stdexcept>
#include <string>

std::string hideBankAccount(const std::string& account) {
    // Validate that the account number is exactly 17 characters long
    if (account.length() != 17) {
        throw std::invalid_argument("Account number must be exactly 17 characters long.");
    }

    // Create the hidden representation with "****" prefix
    const std::string hiddenPart = "****";

    // Extract the visible part of the account number (last 4 characters)
    std::string visiblePart = account.substr(13); // Get last 4 characters

    // Return the formatted string with hidden and visible parts
    return hiddenPart + visiblePart;
}

int main() {
    try {
        std::string account = "12345678901234567";
        std::cout << hideBankAccount(account) << std::endl; // Output: ****4567
    } catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
    }
    return 0;
}