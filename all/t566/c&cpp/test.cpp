#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <ctime>

// Function declaration (assuming it is defined elsewhere)
bool isSameDay(std::time_t timestamp1, std::time_t timestamp2);

TEST_CASE("isSameDay", "[timestamp]") {
    SECTION("should return false for timestamps on different days") {
        std::time_t timestamp1 = std::mktime(new std::tm{0, 0, 10, 1, 9, 124}); // October 1, 2024, 10:00 AM UTC
        std::time_t timestamp2 = std::mktime(new std::tm{0, 0, 10, 2, 9, 124}); // October 2, 2024, 10:00 AM UTC
        REQUIRE(isSameDay(timestamp1, timestamp2) == false);
    }

    SECTION("should return true for timestamps on the same day but different times") {
        std::time_t timestamp1 = std::mktime(new std::tm{0, 0, 0, 1, 9, 124}); // October 1, 2024, 12:00 AM UTC
        std::time_t timestamp2 = std::mktime(new std::tm{0, 30, 12, 1, 9, 124}); // October 1, 2024, 12:30 PM UTC
        REQUIRE(isSameDay(timestamp1, timestamp2) == true);
    }

    SECTION("should return true for timestamps on the same day in different time zones") {
        std::time_t timestamp1 = std::mktime(new std::tm{0, 0, 10, 1, 9, 124}); // UTC
        std::tm tm = {0};
        tm.tm_year = 124; // Year 2024
        tm.tm_mon = 9;    // October
        tm.tm_mday = 1;   // 1st
        tm.tm_hour = 12;  // 12 PM
        tm.tm_min = 0;
        tm.tm_sec = 0;
        tm.tm_isdst = 0;  // Not daylight saving time
        std::time_t timestamp2 = std::mktime(&tm) + 2 * 3600; // UTC+2
        REQUIRE(isSameDay(timestamp1, timestamp2) == true);
    }

    SECTION("should return true for timestamps at midnight on the same day") {
        std::time_t timestamp1 = std::mktime(new std::tm{0, 0, 0, 1, 9, 124}); // October 1, 2024, 12:00 AM UTC
        std::time_t timestamp2 = std::mktime(new std::tm{0, 0, 0, 1, 9, 124}); // Same timestamp
        REQUIRE(isSameDay(timestamp1, timestamp2) == true);
    }

    SECTION("should return false for timestamps in different years") {
        std::time_t timestamp1 = std::mktime(new std::tm{0, 0, 10, 1, 9, 123}); // October 1, 2023, 10:00 AM UTC
        std::time_t timestamp2 = std::mktime(new std::tm{0, 0, 10, 1, 9, 124}); // October 1, 2024, 10:00 AM UTC
        REQUIRE(isSameDay(timestamp1, timestamp2) == false);
    }

    SECTION("should return false for invalid timestamps") {
        std::time_t timestamp1 = -1; // Invalid timestamp
        std::time_t timestamp2 = std::mktime(new std::tm{0, 0, 10, 1, 9, 124}); // Valid timestamp
        REQUIRE(isSameDay(timestamp1, timestamp2) == false);
    }
}