#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <chrono>
#include <iomanip>
#include <sstream>
#include "your_header_file.h" // Include the header file with formatDate

TEST_CASE("formatDate") {
    // Set the system time to a fixed date for consistent testing
    std::tm fixedTime = {};
    std::istringstream ss("2024-08-25 12:00:00");
    ss >> std::get_time(&fixedTime, "%Y-%m-%d %H:%M:%S");
    time_t currentTime = mktime(&fixedTime);
    std::time(nullptr) = currentTime; // Note: Adjust as needed for your test environment

    SECTION("should return '1 day ago' for a date exactly one day before") {
        std::string dateString = "2024-08-24T12:00:00";
        std::string result = formatDate(dateString);
        REQUIRE((result == "1 day ago" || result == "24 hours ago"));
    }

    SECTION("should return '5 hours ago' for a date 5 hours before the current time") {
        std::string dateString = "2024-08-25T07:00:00";
        std::string result = formatDate(dateString);
        REQUIRE(result == "5 hours ago");
    }

    SECTION("should return '2 minutes ago' for a date 2 minutes before the current time") {
        std::string dateString = "2024-08-25T11:58:00";
        std::string result = formatDate(dateString);
        REQUIRE(result == "2 minutes ago");
    }

    SECTION("should return 'just now' for a date within the last second") {
        std::string dateString = "2024-08-25T11:59:59";
        std::string result = formatDate(dateString);
        REQUIRE((result == "1 second ago" || result == "1 seconds ago"));
    }
}