#include <iostream>

int incrementNumber(int num) {
    if (num > 0) {
        return num + 1; // Increment if positive
    }
    return num; // Return original value if non-positive
}

int main() {
    int number;
    std::cout << "Enter a number: ";
    std::cin >> number;
    std::cout << "Result: " << incrementNumber(number) << std::endl;
    return 0;
}