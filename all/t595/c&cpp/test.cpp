TEST_CASE("Test getDaysInMonth function") {
    SECTION("Regular months") {
        REQUIRE(getDaysInMonth(2023, 1) == 31); // January
        REQUIRE(getDaysInMonth(2023, 3) == 31); // March
        REQUIRE(getDaysInMonth(2023, 4) == 30); // April
        REQUIRE(getDaysInMonth(2023, 5) == 31); // May
        REQUIRE(getDaysInMonth(2023, 6) == 30); // June
        REQUIRE(getDaysInMonth(2023, 7) == 31); // July
        REQUIRE(getDaysInMonth(2023, 8) == 31); // August
        REQUIRE(getDaysInMonth(2023, 9) == 30); // September
        REQUIRE(getDaysInMonth(2023, 10) == 31); // October
        REQUIRE(getDaysInMonth(2023, 11) == 30); // November
        REQUIRE(getDaysInMonth(2023, 12) == 31); // December
    }

    SECTION("February in leap year") {
        REQUIRE(getDaysInMonth(2024, 2) == 29); // Leap year
    }

    SECTION("February in non-leap year") {
        REQUIRE(getDaysInMonth(2023, 2) == 28); // Non-leap year
    }
}