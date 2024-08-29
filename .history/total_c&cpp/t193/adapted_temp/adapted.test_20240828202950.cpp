#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
TEST_CASE("InvertBitsToHex Test Cases", "[invertBitsToHex]") {
    // Test Case 1: All bits set
    REQUIRE(invertBitsToHex(0xFFFFFFFF) == "0");

    // Test Case 2: No bits set
    REQUIRE(invertBitsToHex(0x00000000) == "ffffffff");

    // Test Case 3: Random value (0xA5A5A5A5)
    REQUIRE(invertBitsToHex(0xA5A5A5A5) == "5a5a5a5a");

    // Test Case 4: Single bit set (0x80000000)
    REQUIRE(invertBitsToHex(0x80000000) == "7fffffff");

    // Test Case 5: Lower bits set (0x0000FFFF)
    REQUIRE(invertBitsToHex(0x0000FFFF) == "ffff0000");
}
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