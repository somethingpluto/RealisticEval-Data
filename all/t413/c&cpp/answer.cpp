#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// Function to check if a string is a palindrome
bool is_palindrome(const std::string& str) {
    std::string reversed_str = str;
    std::reverse(reversed_str.begin(), reversed_str.end());
    return str == reversed_str;
}

// Function to generate a list of palindrome numbers up to n
std::vector<int> get_palindrome_list(int n) {
    std::vector<int> palindromes;

    for (int i = 0; i < n; ++i) {
        std::string num_str = std::to_string(i);
        if (is_palindrome(num_str)) {
            palindromes.push_back(i);
        }
    }

    return palindromes;
}