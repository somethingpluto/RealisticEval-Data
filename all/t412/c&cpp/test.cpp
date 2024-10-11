TEST_CASE("Math Operations", "[math]") {
    SECTION("Addition") {
        REQUIRE(1 + 1 == 2);
    }

    SECTION("Subtraction") {
        REQUIRE(3 - 1 == 2);
    }

    SECTION("Multiplication") {
        REQUIRE(4 * 2 == 8);
    }

    SECTION("Division") {
        REQUIRE(6 / 3 == 2);
    }
}