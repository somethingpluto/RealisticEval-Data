#include <iostream>

// Function to compute and return the size of an object in bytes.
template<typename T>
size_t size_in_bytes(const T& obj) {
    /**
     * Computes and returns the size of an object in bytes.
     *
     * Args:
     * obj (T): The object to measure the memory size of.
     *
     * Returns:
     * size_t: The size of the object in bytes.
     */
    return sizeof(obj);
}

int main() {
    // Example usage
    int exampleInt = 42;
    std::cout << "Size of int: " << size_in_bytes(exampleInt) << " bytes" << std::endl;

    double exampleDouble = 3.14;
    std::cout << "Size of double: " << size_in_bytes(exampleDouble) << " bytes" << std::endl;

    return 0;
}