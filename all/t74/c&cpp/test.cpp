TEST_CASE("Basic 32-bit conversion") {
    REQUIRE(convert_decimal_to_binary(3.14, 32) == "01000000010010001111010111000011");
}

TEST_CASE("Basic 64-bit conversion") {
    REQUIRE(convert_decimal_to_binary(3.14, 64) == "0100000000001001000111101011100001010001111010111000010100011111");
}

TEST_CASE("Advanced 32-bit conversion") {
    REQUIRE(convert_decimal_to_binary(1.5, 32) == "00111111110000000000000000000000");
}

TEST_CASE("Advanced 64-bit conversion") {
    REQUIRE(convert_decimal_to_binary(1.5, 64) == "0011111111111000000000000000000000000000000000000000000000000000");
}