#include <string>
#include <sstream>
#include <iomanip>
#include <bitset>

/**
 * @brief Inverts the flag bits of an unsigned integer and converts the result to a hexadecimal string.
 *
 * This function takes an unsigned integer as input, inverts its bits (i.e., flips all the bits),
 * and then converts the resulting integer to a hexadecimal string representation.
 *
 * @param value The unsigned integer whose bits are to be inverted.
 * @return A std::string containing the hexadecimal representation of the inverted bits.
 */
std::string invertBitsToHex(unsigned int value) {
    // Invert the bits of the unsigned integer
    unsigned int invertedValue = ~value;

    // Convert the inverted value to a hexadecimal string
    std::stringstream ss;
    ss << std::hex << invertedValue;

    return ss.str();
}