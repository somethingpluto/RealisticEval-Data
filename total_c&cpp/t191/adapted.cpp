#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdint>

std::string floatToHex(float value) {
    // Interpret the float's bit pattern as an unsigned integer
    uint32_t intRepresentation;
    std::memcpy(&intRepresentation, &value, sizeof(value));

    // Convert the unsigned integer to a hexadecimal string
    std::stringstream ss;
    ss << std::setw(8) << std::setfill('0') << std::hex << intRepresentation;

    return ss.str();
}