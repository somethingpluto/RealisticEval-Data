#include <iostream>
#include <string>

int countDashes(const std::string& str) {
    int dashCount = 0;

    for (char c : str) {
        if (c == '-') {
            dashCount++;
        }
    }

    return dashCount;
}

int main() {
    std::string input = "example-string-with-dashes";
    std::cout << "Number of dashes: " << countDashes(input) << std::endl;
    return 0;
}