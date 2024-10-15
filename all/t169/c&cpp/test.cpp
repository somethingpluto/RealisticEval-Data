#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "your_header_file.h" // Include the header where convertToRoman is declared

TEST_CASE("convertToRoman", "[roman]") {
    SECTION("should return the correct Roman numeral for a typical number") {
        std::string result = convertToRoman(1987);
        REQUIRE(result == "MCMLXXXVII"); // 1987 = M + CM + LXXX + VII
    }

    SECTION("should return the correct Roman numeral for the minimum value (1)") {
        std::string result = convertToRoman(1);
        REQUIRE(result == "I"); // 1 = I
    }

    SECTION("should return the correct Roman numeral for a large number (3999)") {
        std::string result = convertToRoman(3999);
        REQUIRE(result == "MMMCMXCIX"); // 3999 = MMM + CM + XC + IX
    }

    SECTION("should return the correct Roman numeral for a number with different numeral repeats") {
        std::string result = convertToRoman(1666);
        REQUIRE(result == "MDCLXVI"); // 1666 = M + D + CLX + VI
    }

    SECTION("should return the correct Roman numeral for number with no 5s and 1s") {
        std::string result = convertToRoman(2000);
        REQUIRE(result == "MM"); // 2000 = MM
    }
}