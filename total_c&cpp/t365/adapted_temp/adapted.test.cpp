#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
TEST_CASE("Day of Week Calculation", "[day_of_week]") {
    REQUIRE(day_of_week(2024, 1, 1) == 1);  // January 1, 2024 is a Monday
    REQUIRE(day_of_week(2023, 8, 29) == 2);  // August 29, 2023 is a Tuesday
    REQUIRE(day_of_week(2022, 12, 25) == 7); // December 25, 2022 is a Sunday
    REQUIRE(day_of_week(1989, 11, 9) == 4);  // November 9, 1989 is a Thursday
    REQUIRE(day_of_week(2000, 2, 29) == 2);  // February 29, 2000 is a Tuesday
}