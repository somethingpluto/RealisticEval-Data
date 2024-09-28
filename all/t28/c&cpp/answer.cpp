#include <iostream>
#include <vector>
#include <bitset>

void print_memory_bits(const std::vector<uint8_t>& memory_section) {
    /*
    Prints the status of each bit (0 or 1) in the given section of memory.
    Print format example:
    Byte 0: 1 1 0 0 1 1 0 0
    Byte 1: 1 1 1 1 0 0 0 0

    :param memory_section: std::vector<uint8_t> representing the section of memory to be read.
    */

    for (size_t byte_index = 0; byte_index < memory_section.size(); ++byte_index) {
        std::cout << "Byte " << byte_index << ": ";
        uint8_t byte = memory_section[byte_index];
        
        for (int bit_index = 7; bit_index >= 0; --bit_index) {
            // Shift the bit to the right and check the least significant bit
            int bit_status = (byte >> bit_index) & 1;
            std::cout << bit_status << " ";
        }
        std::cout << std::endl;  // Newline after each byte
    }
}

int main() {
    // Test data: {0b11001100, 0b11110000}
    std::vector<uint8_t> memory_section = {0xCC, 0xF0};
    print_memory_bits(memory_section);
    return 0;
}