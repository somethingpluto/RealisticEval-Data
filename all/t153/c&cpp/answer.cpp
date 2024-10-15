#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

std::string compressHash(const std::string& hash) {
    // Convert the hash string to a number in base 16 (hexadecimal)
    unsigned long long num = std::stoull(hash, nullptr, 16);

    // Define the base and alphabet for encoding
    const int base = 62;
    const std::string alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // Initialize the result string
    std::string result;

    // Convert the number to the desired base (base 62) and construct the compressed string
    while (result.length() < 5) {
        int remainder = num % base;
        result += alphabet[remainder];
        num /= base;
    }

    return result;
}