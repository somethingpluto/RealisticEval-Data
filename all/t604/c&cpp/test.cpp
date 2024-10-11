
TEST_CASE("Power function test cases") {
    SECTION("Base cases") {
        // Test 0^0, should return 1 (by convention)
        REQUIRE(power_tail(0, 0) == 1);

        // Test x^0 for any x, should return 1
        REQUIRE(power_tail(5, 0) == 1);
        REQUIRE(power_tail(12345, 0) == 1);
    }

    SECTION("Power of one") {
        // Test 1^y for any y, should return 1
        REQUIRE(power_tail(1, 5) == 1);
        REQUIRE(power_tail(1, 123) == 1);
    }

    SECTION("Power of zero") {
        // Test 0^y for any y > 0, should return 0
        REQUIRE(power_tail(0, 5) == 0);
        REQUIRE(power_tail(0, 100) == 0);
    }

    SECTION("Positive powers") {
        // Test some positive powers
        REQUIRE(power_tail(2, 3) == 8);     // 2^3 = 8
        REQUIRE(power_tail(3, 4) == 81);    // 3^4 = 81
        REQUIRE(power_tail(5, 2) == 25);     // 5^2 = 25
    }
}