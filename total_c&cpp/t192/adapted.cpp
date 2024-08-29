#include <iostream>
#include <string>
#include <sstream>

unsigned int hexStringToUnsignedInt(const std::string& hexString) {
    unsigned int result;
    std::stringstream ss;
    ss << std::hex << hexString;
    ss >> result;
    return result;
}