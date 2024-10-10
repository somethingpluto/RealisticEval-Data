TEST_CASE("Extract character bits", "[extractCharacterBits]") {
    SECTION("Character found") {
        std::vector<unsigned char> byteArray = {0x68, 0x65, 0x6c, 0x6c, 0x6f};  // "hello"
        std::string charStr = "l";
        auto result = extractCharacterBits(byteArray, charStr);

        REQUIRE(result.has_value());
        REQUIRE(result->first == 3);  // Position of 'l' in the byte array
        REQUIRE(result->second == "110111");  // Binary representation of 'l'
    }

    SECTION("Character not found") {
        std::vector<unsigned char> byteArray = {0x68, 0x65, 0x6c, 0x6c, 0x6f};  // "hello"
        std::string charStr = "z";
        auto result = extractCharacterBits(byteArray, charStr);

        REQUIRE(!result.has_value());
    }
}