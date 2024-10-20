TEST_CASE("Test bits_to_bytes function", "[bits_to_bytes]") {
    SECTION("Test exact multiple of eight") {
        std::vector<int> bits = {1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1};
        std::vector<unsigned char> expected = {0b10110010, 0b01001111};
        auto result = bits_to_bytes(bits);
        REQUIRE(result == expected);
    }

    SECTION("Test incomplete byte discarded") {
        std::vector<int> bits = {1, 0, 1, 1, 0, 0, 1, 0, 0, 1};  // Last two bits should be discarded
        std::vector<unsigned char> expected = {0b10110010};
        auto result = bits_to_bytes(bits);
        REQUIRE(result == expected);
    }

    SECTION("Test empty bit array") {
        std::vector<int> bits = {};
        std::vector<unsigned char> expected = {};
        auto result = bits_to_bytes(bits);
        REQUIRE(result == expected);
    }

    SECTION("Test single full byte") {
        std::vector<int> bits = {1, 1, 1, 1, 1, 1, 1, 1};  // Represents the byte 0xFF
        std::vector<unsigned char> expected = {0xFF};
        auto result = bits_to_bytes(bits);
        REQUIRE(result == expected);
    }

    SECTION("Test no bits discarded") {
        std::vector<int> bits = {1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1};
        std::vector<unsigned char> expected = {0xCC, 0x77};  // Corrected the second byte from 0xB7 to 0x77
        auto result = bits_to_bytes(bits);
        REQUIRE(result == expected);
    }
}