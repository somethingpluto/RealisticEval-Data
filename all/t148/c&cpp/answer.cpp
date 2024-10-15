#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <cstdint>

// Function to decode a base64 string
std::string base64Decode(const std::string &base64) {
    static const std::string base64_chars =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789+/";

    std::string result;
    int in_len = base64.size();
    int i = 0;
    int j = 0;

    std::vector<uint8_t> buffer(3);
    uint32_t val = 0;

    while (in_len-- && (base64[i] != '=') && (base64[i] != ' ')) {
        val = (val << 6) + base64_chars.find(base64[i++]);
        if (++j == 4) {
            for (j = 0; j < 3; j++) {
                result.push_back((val >> (16 - j * 8)) & 0xFF);
            }
            val = 0;
            j = 0;
        }
    }

    if (j) {
        for (int k = j; k < 4; k++) {
            val <<= 6;
        }
        for (j = 0; j < 3; j++) {
            if (j < (k - 1)) {
                result.push_back((val >> (16 - j * 8)) & 0xFF);
            }
        }
    }

    return result;
}

std::vector<uint8_t> base64ToArrayBuffer(const std::string &base64) {
    std::string binaryString = base64Decode(base64);
    std::vector<uint8_t> buffer(binaryString.begin(), binaryString.end());
    return buffer;
}