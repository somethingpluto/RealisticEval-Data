#include <string>
#include <sstream>
#include <iomanip>
#include <bitset>

/**
 * @brief Invert the flag bits of an unsigned integer to a hexadecimal string. The number of bits is not complete by 0
 *
 * @param value The unsigned integer whose bits are to be inverted.
 * @return A std::string containing the hexadecimal representation of the inverted bits.
 */
std::string convFlags(unsigned int value) {
    // Create a mask for the first five bits (0x1F = 00011111)
    unsigned int mask = 0x1F;

    // Invert the first five bits using XOR
    unsigned int invertedValue = value ^ mask;

    // Convert the result to a hexadecimal string
    std::stringstream ss;
    ss << std::hex << invertedValue;

    return ss.str();
}