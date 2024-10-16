#include <iostream>
#include <regex>
#include <string>

bool isSnakeCase(const std::string& input) {
    // Regular expression to match SNAKE_CASE
    std::regex snakeCaseRegex("^[a-z]+(_[a-z]+)*$");
    return std::regex_match(input, snakeCaseRegex);
}

int main() {
    std::string testString;
    std::cout << "Enter a string to check if it's in SNAKE_CASE: ";
    std::cin >> testString;

    if (isSnakeCase(testString)) {
        std::cout << testString << " is in SNAKE_CASE." << std::endl;
    } else {
        std::cout << testString << " is not in SNAKE_CASE." << std::endl;
    }

    return 0;
}