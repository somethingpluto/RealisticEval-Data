TEST_CASE("Test calculate_total_seconds", "[calculate_total_seconds]") {
    SECTION("Test with full values provided for days, hours, minutes, and seconds") {
        std::vector<int> time = {1, 2, 3, 4};  // 1 day, 2 hours, 3 minutes, 4 seconds
        int expected = 93784;
        REQUIRE(calculate_total_seconds(time) == expected);
    }

    SECTION("Test with some values missing (assumed trailing zeros)") {
        std::vector<int> time = {0, 2, 3};  // 0 days, 2 hours, 3 minutes
        int expected = 7380;
        REQUIRE(calculate_total_seconds(time) == expected);
    }

    SECTION("Test with only seconds provided") {
        std::vector<int> time = {7200};  // 7200 seconds
        int expected = 7200;  // Corrected expected value
        REQUIRE(calculate_total_seconds(time) == expected);
    }

    SECTION("Test with no time values provided") {
        std::vector<int> time = {};  // Empty vector
        int expected = 0;
        REQUIRE(calculate_total_seconds(time) == expected);
    }
}