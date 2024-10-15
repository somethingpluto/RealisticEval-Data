TEST_CASE("formatNumber") {
    SECTION("should format numbers greater than or equal to 1,000,000 with 'M' suffix") {
        REQUIRE(formatNumber(1500000) == "1.5M");
        REQUIRE(formatNumber(1000000) == "1.0M");
    }

    SECTION("should format numbers greater than or equal to 1,000 but less than 1,000,000 with 'K' suffix") {
        REQUIRE(formatNumber(2500) == "2.5K");
        REQUIRE(formatNumber(1000) == "1.0K");
    }

    SECTION("should return the number as a string if it is less than 1,000") {
        REQUIRE(formatNumber(999) == "999");
        REQUIRE(formatNumber(500) == "500");
    }

    SECTION("should handle edge cases like exactly 1,000 or 1,000,000") {
        REQUIRE(formatNumber(1000) == "1.0K");
        REQUIRE(formatNumber(1000000) == "1.0M");
    }
}