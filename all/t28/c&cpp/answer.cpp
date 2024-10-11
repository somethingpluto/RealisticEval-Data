#include <iostream>
#include <vector>

void print_memory_bits(const std::vector<unsigned char>& memory_section) {
    for (unsigned char byte : memory_section) {
        for (int i = 7; i >= 0; i--) {
            std::cout << ((byte >> i) & 1);
        }
        std::cout << std::endl;
    }
}