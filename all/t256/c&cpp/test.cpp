TEST_CASE("bits_to_bytes", "[bits_to_bytes]") {
    SECTION("Empty input") {
        REQUIRE(bits_to_bytes({}) == std::vector<uint8_t>{});
    }

    SECTION("Multiple of 8 bits") {
        REQUIRE(bits_to_bytes({1, 0, 1, 0, 1, 0, 1, 0}) == std::vector<uint8_t>{0b10101010});
    }

    SECTION("Not multiple of 8 bits") {
        REQUIRE(bits_to_bytes({1, 0, 1, 0, 1, 0, 1, 0, 1}) == std::vector<uint8_t>{0b10101010});
    }

    SECTION("Non-binary values") {
        CHECK_THROWS_WITH(bits_to_bytes({1, 0, 2, 0, 1}), "Input contains non-binary values");
    }
}