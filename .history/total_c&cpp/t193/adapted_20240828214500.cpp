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
    // Invert the bits of the unsigned integer
    unsigned int invertedValue = ~value;

    // Convert the inverted value to a hexadecimal string
    std::stringstream ss;
    ss << std::hex << invertedValue;

    return ss.str();
}