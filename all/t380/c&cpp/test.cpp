TEST_CASE("Calculate Total Seconds", "[time]") {
    SECTION("Days, Hours, Minutes, Seconds") {
        REQUIRE(calculate_total_seconds(std::make_tuple(1, 2, 3, 4)) == 93784);
    }

    SECTION("Hours, Minutes, Seconds") {
        REQUIRE(calculate_total_seconds(std::make_tuple(0, 2, 3)) == 7380);
    }

    SECTION("Only Days") {
        REQUIRE(calculate_total_seconds(std::make_tuple(1, 0, 0, 0)) == 86400);
    }

    SECTION("Only Hours") {
        REQUIRE(calculate_total_seconds(std::make_tuple(0, 1, 0, 0)) == 3600);
    }

    SECTION("Only Minutes") {
        REQUIRE(calculate_total_seconds(std::make_tuple(0, 0, 1, 0)) == 60);
    }

    SECTION("Only Seconds") {
        REQUIRE(calculate_total_seconds(std::make_tuple(0, 0, 0, 1)) == 1);
    }

    SECTION("All Zeroes") {
        REQUIRE(calculate_total_seconds(std::make_tuple(0, 0, 0, 0)) == 0);
    }
}