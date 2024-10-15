#include <iostream>
#include <string>
#include <cctype>

int countLetters(const std::string& str) {
    int count = 0;
    for (char ch : str) {
        if (std::isalpha(ch)) {  // Check if the character is a letter
            count++;
        }
    }
    return count;
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int letterCount = countLetters(input);
    std::cout << "Number of letters: " << letterCount << std::endl;
    return 0;
}