#include <iostream>

int main() {
    int num = 42;
    int* ptr = &num;

    // Print the size of the integer
    std::cout << "Size of integer: " << sizeof(num) << std::endl;

    // Print the size of the pointer
    std::cout << "Size of pointer: " << sizeof(ptr) << std::endl;

    return 0;
}