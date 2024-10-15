#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <chrono>
#include <iomanip>
#include <sstream>
#include <string>

// Assuming getRelativeTime is defined elsewhere
std::string getRelativeTime(const std::chrono::system_clock::time_point& messageDate);

TEST_CASE("getRelativeTime", "[time]") {
    // Mock the current date
    auto mockNow = std::chrono::system_clock::time_point(std::chrono::seconds(1729468800)); // 2024-10-01

    SECTION("should return 'Today' for a message created today") {
        auto messageDate = mockNow; // Current date
        REQUIRE(getRelativeTime(messageDate) == "Today");
    }

    SECTION("should return 'Yesterday' for a message created yesterday") {
        auto messageDate = mockNow - std::chrono::hours(24); // Yesterday
        REQUIRE(getRelativeTime(messageDate) == "Yesterday");
    }

    SECTION("should return formatted date string for a message created 10 days ago") {
        auto messageDate = mockNow - std::chrono::hours(24 * 10); // 10 days ago
        REQUIRE(getRelativeTime(messageDate) == "2024/09/21"); // Adjust based on the mock date
    }

    SECTION("should return formatted date string for a message created 15 days ago") {
        auto messageDate = mockNow - std::chrono::hours(24 * 15); // 15 days ago
        REQUIRE(getRelativeTime(messageDate) == "2024/09/16"); // Adjust based on the mock date
    }
}