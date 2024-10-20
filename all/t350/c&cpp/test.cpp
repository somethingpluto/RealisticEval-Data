TEST_CASE("Test byte_array_to_hex_string function") {
    
    SECTION("Empty byte array") {
        std::vector<unsigned char> input_data;  // Empty byte array
        REQUIRE(byte_array_to_hex_string(input_data) == "");
    }

    SECTION("Single byte") {
        std::vector<unsigned char> input_data = {0x0F};  // 15 in decimal
        std::string result = byte_array_to_hex_string(input_data);
        REQUIRE(result == "0F" || result == "0f");
    }

    SECTION("Multiple bytes") {
        std::vector<unsigned char> input_data = {0x01, 0x0A, 0xFF};
        std::string result = byte_array_to_hex_string(input_data);
        REQUIRE(result == "010aff" || result == "010AFF");
    }

    SECTION("Zero bytes") {
        std::vector<unsigned char> input_data = {0x00, 0x00, 0x00};
        REQUIRE(byte_array_to_hex_string(input_data) == "000000");
    }

    SECTION("Negative bytes") {
        std::vector<unsigned char> input_data = {0x80, 0xFF};  // 128 and 255
        std::string result = byte_array_to_hex_string(input_data);
        REQUIRE(result == "80FF" || result == "80ff");
    }
}