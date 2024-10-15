#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>
#include <string>

std::string boolArrayToBinaryString(const std::vector<bool>& boolArray);

TEST_CASE("boolArrayToBinaryString") {
    SECTION("converts an array of all true values") {
        std::vector<bool> boolArray = {true, true, true};
        std::string expected = "111";
        REQUIRE(boolArrayToBinaryString(boolArray) == expected);
    }

    SECTION("converts an array of all false values") {
        std::vector<bool> boolArray = {false, false, false};
        std::string expected = "000";
        REQUIRE(boolArrayToBinaryString(boolArray) == expected);
    }

    SECTION("converts an array with a mix of true and false values") {
        std::vector<bool> boolArray = {true, false, true, false};
        std::string expected = "1010";
        REQUIRE(boolArrayToBinaryString(boolArray) == expected);
    }

    SECTION("handles an empty array") {
        std::vector<bool> boolArray = {};
        std::string expected = "";
        REQUIRE(boolArrayToBinaryString(boolArray) == expected);
    }

    SECTION("handles a single boolean value") {
        std::vector<bool> boolArray = {true};
        std::string expected = "1";
        REQUIRE(boolArrayToBinaryString(boolArray) == expected);
    }
}