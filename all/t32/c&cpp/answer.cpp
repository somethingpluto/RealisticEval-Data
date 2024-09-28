#include <iostream>
#include <vector>

class CRC64 {
public:
    static const uint64_t POLY64REV = 0xC96C5795D7870F42;
    static std::vector<uint64_t> crc64_tab;

    static void crc64_init_table() {
        if (crc64_tab.empty()) {
            crc64_tab.resize(256);
            for (int b = 0; b < 256; ++b) {
                uint64_t crc = b;
                for (int j = 0; j < 8; ++j) {
                    if (crc & 1) {
                        crc = (crc >> 1) ^ POLY64REV;
                    } else {
                        crc >>= 1;
                    }
                }
                crc64_tab[b] = crc;
            }
        }
    }

    static uint64_t crc64_update(uint64_t crc, uint8_t byte) {
        int tbl_idx = (crc ^ byte) & 0xFF;
        return (crc64_tab[tbl_idx] ^ (crc >> 8)) & 0xFFFFFFFFFFFFFFFF;
    }

    static uint64_t compute(int64_t input_integer) {
        crc64_init_table();

        if (input_integer < 0) {
            input_integer = (1ULL << 64) + input_integer;
        }

        uint64_t crc = 0xFFFFFFFFFFFFFFFF;
        uint8_t input_bytes[8];
        for (int i = 0; i < 8; ++i) {
            input_bytes[i] = (input_integer >> (8 * i)) & 0xFF;
        }

        for (auto b : input_bytes) {
            crc = crc64_update(crc, b);
        }

        return crc ^ 0xFFFFFFFFFFFFFFFF;
    }
};

std::vector<uint64_t> CRC64::crc64_tab;

int main() {
    int64_t input = 123456789; // Example input
    uint64_t crc = CRC64::compute(input);
    std::cout << "CRC64: " << std::hex << crc << std::endl;
    return 0;
}