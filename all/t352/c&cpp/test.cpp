TEST_CASE("Hex string to byte array conversion") {
    
    SECTION("Normal hex string") {
        std::string hex_str = "1a3f";
        std::vector<uint8_t> expected = {0x1A, 0x3F};
        REQUIRE(hex_string_to_byte_array(hex_str) == expected);
    }

    SECTION("Odd length hex string") {
        std::string hex_str = "123";
        std::vector<uint8_t> expected = {0x01, 0x23};
        REQUIRE(hex_string_to_byte_array(hex_str) == expected);
    }

    SECTION("Empty string") {
        std::string hex_str = "";
        std::vector<uint8_t> expected = {};
        REQUIRE(hex_string_to_byte_array(hex_str) == expected);
    }

    SECTION("Hex string with uppercase") {
        std::string hex_str = "1A3F";
        std::vector<uint8_t> expected = {0x1A, 0x3F};
        REQUIRE(hex_string_to_byte_array(hex_str) == expected);
    }
}