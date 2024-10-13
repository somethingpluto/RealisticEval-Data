#include <iostream>
#include <vector>
#include <bitset>

// Function to print the status of each bit (0 or 1) in the given section of memory.
void print_memory_bits(const std::vector<uint8_t>& memory_section) {
    for (uint8_t byte : memory_section) {
        for (int i = 7; i >= 0; --i) {
            uint8_t bit = (byte >> i) & 1;
            std::cout << bit;
        }
        std::cout << std::endl;
    }
}

int main() {
    // Example usage
    std::vector<uint8_t> memory_section = {0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80};
    print_memory_bits(memory_section);
    return 0;
}