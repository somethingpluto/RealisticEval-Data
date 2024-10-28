#include <iostream>
#include <iomanip>
#include <bitset>
#include <stdexcept>
#include <cstring>

std::string convert_decimal_to_binary(double decimal_value, int bit_length) {
    if (bit_length != 32 && bit_length != 64) {
        throw std::invalid_argument("Invalid bit length. Please specify either 32 or 64.");
    }

    std::string binary_representation;

    if (bit_length == 32) {
        // Convert the decimal to a 32-bit binary representation
        float value = static_cast<float>(decimal_value);
        uint32_t packed_value;
        std::memcpy(&packed_value, &value, sizeof(value));  // Pack as 32-bit float
        binary_representation = std::bitset<32>(packed_value).to_string();  // Convert to binary string
    } else if (bit_length == 64) {
        // Convert the decimal to a 64-bit binary representation
        uint64_t packed_value;
        std::memcpy(&packed_value, &decimal_value, sizeof(decimal_value));  // Pack as 64-bit double
        binary_representation = std::bitset<64>(packed_value).to_string();  // Convert to binary string
    }

    return binary_representation;
}

int main() {
    try {
        std::cout << "Binary representation of 10.75 in 32 bits: "
                  << convert_decimal_to_binary(10.75, 32) << std::endl;
        std::cout << "Binary representation of 10.75 in 64 bits: "
                  << convert_decimal_to_binary(10.75, 64) << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    
    return 0;
}
