#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <ctime>

// Assuming findNthWeekdayOfSpecificYear function is implemented as in the previous conversion

std::tm make_tm(int year, int month, int day) {
    std::tm timeStruct = {};
    timeStruct.tm_year = year - 1900;
    timeStruct.tm_mon = month - 1;
    timeStruct.tm_mday = day;
    std::mktime(&timeStruct); // normalize
    return timeStruct;
}

TEST_CASE("TestFindNthWeekdayOfSpecificYear") {

    SECTION("test_regular_occurrence") {
        // Test for the 2nd Monday of May 2023
        std::tm result = findNthWeekdayOfSpecificYear(2023, 5, 2, 0);
        std::tm expected = make_tm(2023, 5, 8);
        REQUIRE(result.tm_year == expected.tm_year);
        REQUIRE(result.tm_mon == expected.tm_mon);
        REQUIRE(result.tm_mday == expected.tm_mday);
    }

    SECTION("test_last_occurrence") {
        // Test for the 5th Monday of May 2023, which doesn't exist, should return the last Monday
        std::tm result = findNthWeekdayOfSpecificYear(2023, 5, 5, 0);
        std::tm expected = make_tm(2023, 5, 29);
        REQUIRE(result.tm_year == expected.tm_year);
        REQUIRE(result.tm_mon == expected.tm_mon);
        REQUIRE(result.tm_mday == expected.tm_mday);
    }

    SECTION("test_out_of_range") {
        // Test for the 10th Monday of May 2023, which definitely doesn't exist, should return the last Monday
        std::tm result = findNthWeekdayOfSpecificYear(2023, 5, 10, 0);
        std::tm expected = make_tm(2023, 5, 29);
        REQUIRE(result.tm_year == expected.tm_year);
        REQUIRE(result.tm_mon == expected.tm_mon);
        REQUIRE(result.tm_mday == expected.tm_mday);
    }

    SECTION("test_first_day_is_weekday") {
        // Test for when the first day of the month is the weekday in question, 1st Tuesday of August 2023
        std::tm result = findNthWeekdayOfSpecificYear(2023, 8, 1, 1);
        std::tm expected = make_tm(2023, 8, 1);
        REQUIRE(result.tm_year == expected.tm_year);
        REQUIRE(result.tm_mon == expected.tm_mon);
        REQUIRE(result.tm_mday == expected.tm_mday);
    }

    SECTION("test_edge_year_transition") {
        // Test for the 1st Friday of December 2023, checking the transition to a new year boundary condition
        std::tm result = findNthWeekdayOfSpecificYear(2023, 12, 1, 4);
        std::tm expected = make_tm(2023, 12, 1);
        REQUIRE(result.tm_year == expected.tm_year);
        REQUIRE(result.tm_mon == expected.tm_mon);
        REQUIRE(result.tm_mday == expected.tm_mday);
    }
}