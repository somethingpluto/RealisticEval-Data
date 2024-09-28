#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>

class CRC64 {
public:
    static const uint64_t POLY64REV;
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

const uint64_t CRC64::POLY64REV = 0xC96C5795D7870F42;
std::vector<uint64_t> CRC64::crc64_tab;

TEST_CASE("CRC64 Initialization", "[CRC64]") {
    CRC64::crc64_init_table();
    REQUIRE(CRC64::crc64_tab.size() == 256);
    REQUIRE(std::all_of(CRC64::crc64_tab.begin(), CRC64::crc64_tab.end(), [](uint64_t x) { return x != 0; }));
}

TEST_CASE("CRC64 Update", "[CRC64]") {
    CRC64::crc64_init_table();
    uint64_t initial_crc = 0xFFFFFFFFFFFFFFFF;
    uint8_t byte = 0x01;
    uint64_t updated_crc = CRC64::crc64_update(initial_crc, byte);
    uint64_t expected_crc = (CRC64::crc64_tab[0xFE] ^ (initial_crc >> 8)) & 0xFFFFFFFFFFFFFFFF;
    REQUIRE(updated_crc == expected_crc);
}

TEST_CASE("CRC64 Compute Positive Integer", "[CRC64]") {
    uint64_t result = CRC64::compute(1234567890);
    uint64_t expected_result = 0xB0F9361BAEB8A24E;
    REQUIRE(result == expected_result);
}

TEST_CASE("CRC64 Compute Negative Integer", "[CRC64]") {
    uint64_t result = CRC64::compute(-1234567890);
    uint64_t expected_result = 0x865B548A1C95DB76;
    REQUIRE(result == expected_result);
}

TEST_CASE("CRC64 Compute Zero", "[CRC64]") {
    uint64_t result = CRC64::compute(0);
    uint64_t expected_result = 0xB90956C775A41001;  // Example result for CRC64 of zero
    REQUIRE(result == expected_result);
}