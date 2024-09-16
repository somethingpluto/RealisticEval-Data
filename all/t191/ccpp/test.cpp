TEST_CASE("floatToHex tests", "[floatToHex]") {
    SECTION("Test with positive float 123.456") {
        float input = 123.456f;
        std::string expected = "42f6e979";
        REQUIRE(floatToHex(input) == expected);
    }

    SECTION("Test with negative float -123.456") {
        float input = -123.456f;
        std::string expected = "c2f6e979";
        REQUIRE(floatToHex(input) == expected);
    }

    SECTION("Test with zero") {
        float input = 0.0f;
        std::string expected = "00000000";
        REQUIRE(floatToHex(input) == expected);
    }

    SECTION("Test with small positive float 0.0001") {
        float input = 0.0001f;
        std::string expected = "38d1b717";
        REQUIRE(floatToHex(input) == expected);
    }

    SECTION("Test with large float 1e30") {
        float input = 1e30f;
        std::string expected = "7149f2ca";
        REQUIRE(floatToHex(input) == expected);
    }
}