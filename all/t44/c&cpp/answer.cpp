#include <iostream>
#include <string>
#include <utility> // For std::pair

// Function to align two lines of string to the left, supplementing with spaces if the length is not enough
std::pair<std::string, std::string> align_lines_left(const std::string& str1, const std::string& str2) {
    // Determine the maximum length of the two strings
    size_t max_length = std::max(str1.length(), str2.length());

    // Align both strings to the left by padding with spaces
    std::string aligned_str1 = str1;
    std::string aligned_str2 = str2;

    aligned_str1.append(max_length - str1.length(), ' ');
    aligned_str2.append(max_length - str2.length(), ' ');

    return {aligned_str1, aligned_str2};
}

int main() {
    // Example usage
    std::string str1 = "Hello";
    std::string str2 = "World!";
    auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);

    std::cout << "Aligned str1: " << aligned_str1 << std::endl;
    std::cout << "Aligned str2: " << aligned_str2 << std::endl;

    return 0;
}