#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "your_header_file.h" // Include the header file where your function is declared

TEST_CASE("convertTimeHmsStringToMs", "[conversion]") {
    SECTION("converts typical time string correctly (1h30m15s)") {
        long long result = convertTimeHmsStringToMs("1h30m15s");
        REQUIRE(result == 5415000);  // 1 hour + 30 minutes + 15 seconds in ms
    }

    SECTION("correctly converts string with zero values (0h0m0s)") {
        long long result = convertTimeHmsStringToMs("0h0m0s");
        REQUIRE(result == 0);  // 0 ms
    }

    SECTION("converts maximum single digit values (9h59m59s)") {
        long long result = convertTimeHmsStringToMs("9h59m59s");
        REQUIRE(result == 35999000); // 9 hours + 59 minutes + 59 seconds in ms
    }

    SECTION("handles large values (100h0m0s)") {
        long long result = convertTimeHmsStringToMs("100h0m0s");
        REQUIRE(result == 360000000); // 100 hours in ms
    }

    SECTION("correctly converts strings with leading zeros (01h01m01s)") {
        long long result = convertTimeHmsStringToMs("01h01m01s");
        REQUIRE(result == 3661000); // 1 hour + 1 minute + 1 second in ms
    }
}