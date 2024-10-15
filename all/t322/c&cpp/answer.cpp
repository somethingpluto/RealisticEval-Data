#include <iostream>
#include <regex>
#include <string>

bool isValidEmail(const std::string& email) {
    // Define the regular expression for a valid email
    std::regex emailRegex("^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$");

    // Test the email against the regular expression
    return std::regex_match(email, emailRegex);
}

int main() {
    std::string email = "example@example.com";
    std::cout << (isValidEmail(email) ? "Valid email" : "Invalid email") << std::endl;
    return 0;
}