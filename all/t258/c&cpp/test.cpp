TEST_CASE("Test extract_character_bits function", "[extract_character_bits]") {
    SECTION("test_case_1_valid_utf8") {
        std::vector<unsigned char> byte_array = {'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'};
        char char_to_find = 'W';
        auto result = extract_character_bits(byte_array, char_to_find, "utf-8");
        auto expected_result = std::make_pair(7, "01010111");
        REQUIRE(result == expected_result);
    }

    SECTION("test_case_2_non_existent_character") {
        std::vector<unsigned char> byte_array = {'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', '.'};
        char char_to_find = 'z';
        auto result = extract_character_bits(byte_array, char_to_find, "utf-8");
        REQUIRE(result.first == -1 && result.second.empty());
    }

    SECTION("test_case_3_invalid_encoding") {
        std::vector<unsigned char> byte_array = {0xff, 0xfe};
        char char_to_find = 'A';
        auto result = extract_character_bits(byte_array, char_to_find, "ascii");
        REQUIRE(result.first == -1 && result.second.empty());
    }

    SECTION("test_case_4_valid_utf16") {
        std::vector<unsigned char> byte_array = {
            0xff, 0xfe, 0x00, 0x48, 0x00, 0x65, 0x00, 0x6c,
            0x00, 0x6c, 0x00, 0x6f, 0x00, 0x2c, 0x00, 0x20,
            0x00, 0x57, 0x00, 0x6f, 0x00, 0x72, 0x00, 0x6c,
            0x00, 0x64, 0x00, 0x21
        };
        char char_to_find = '!';
        auto result = extract_character_bits(byte_array, char_to_find, "utf-16");
        auto expected_result = std::make_pair(12, "00100001 00000000");
        REQUIRE(result == expected_result);
    }

    SECTION("test_case_5_special_characters_utf8") {
        std::vector<unsigned char> byte_array = {
            'P', 'y', 't', 'h', 'o', 'n', 0xf0, 0x9f, 0x90, 0xb0, ' ', 'i', 's', ' ', 'f', 'u', 'n', '!'
        };
        char char_to_find = '\xf0\x9f\x90\xb0'; // Unicode character 🐍 in UTF-8
        auto result = extract_character_bits(byte_array, char_to_find, "utf-8");
        auto expected_result = std::make_pair(7, "11110000 10011111 10010000 10001101");
        REQUIRE(result == expected_result);
    }
}