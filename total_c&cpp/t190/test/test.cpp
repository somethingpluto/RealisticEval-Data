TEST_CASE("Hexadecimal String to Float Conversion", "[hexStringToFloat]") {

    SECTION("Positive number: 40490FDB") {
        std::string hexStr = "40490FDB"; // 3.14159 in float
        float result = hexStringToFloat(hexStr);
        REQUIRE(result == Approx(3.14159f).epsilon(0.00001f));
    }

    SECTION("Negative number: C0490FDB") {
        std::string hexStr = "C0490FDB"; // -3.14159 in float
        float result = hexStringToFloat(hexStr);
        REQUIRE(result == Approx(-3.14159f).epsilon(0.00001f));
    }

    SECTION("Zero: 00000000") {
        std::string hexStr = "00000000"; // 0.0 in float
        float result = hexStringToFloat(hexStr);
        REQUIRE(result == Approx(0.0f).epsilon(0.00001f));
    }

    SECTION("Small positive number: 3F800000") {
        std::string hexStr = "3F800000"; // 1.0 in float
        float result = hexStringToFloat(hexStr);
        REQUIRE(result == Approx(1.0f).epsilon(0.00001f));
    }

    SECTION("Small negative number: BF800000") {
        std::string hexStr = "BF800000"; // -1.0 in float
        float result = hexStringToFloat(hexStr);
        REQUIRE(result == Approx(-1.0f).epsilon(0.00001f));
    }
}