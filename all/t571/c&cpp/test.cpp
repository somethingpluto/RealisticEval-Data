#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

// Assume isValidCoordinate is defined elsewhere

TEST_CASE("isValidCoordinate") {
    SECTION("valid latitude with direction") {
        std::string coord = "45.123N";
        REQUIRE(isValidCoordinate(coord) == true);
    }

    SECTION("valid latitude without direction") {
        std::string coord = "90.0";
        REQUIRE(isValidCoordinate(coord) == true);
    }

    SECTION("valid longitude with direction") {
        std::string coord = "180.0E";
        REQUIRE(isValidCoordinate(coord) == true);
    }

    SECTION("valid longitude without direction") {
        std::string coord = "-120.456";
        REQUIRE(isValidCoordinate(coord) == true);
    }

    SECTION("invalid longitude exceeding range") {
        std::string coord = "-200.5";
        REQUIRE(isValidCoordinate(coord) == false);
    }
}