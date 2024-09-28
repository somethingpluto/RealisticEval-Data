#include <iostream>

template <typename T>
size_t size_in_bytes(const T& obj) {
    return sizeof(obj);
}

int main() {
    int myInt = 42;
    double myDouble = 42.0;
    std::string myString = "Hello, World!";

    std::cout << "Size of int: " << size_in_bytes(myInt) << " bytes" << std::endl;
    std::cout << "Size of double: " << size_in_bytes(myDouble) << " bytes" << std::endl;
    std::cout << "Size of string: " << size_in_bytes(myString) << " bytes (not including dynamic content)" << std::endl;

    return 0;
}