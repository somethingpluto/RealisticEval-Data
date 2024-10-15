#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <stdexcept>

// Assuming the calculateFinalPrice function is declared above or in another included file

TEST_CASE("calculateFinalPrice", "[calculateFinalPrice]") {
    SECTION("should calculate the final price correctly with valid inputs") {
        double result = calculateFinalPrice("200", "10");
        REQUIRE(result == 180);
    }

    SECTION("should return the original price when the discount is 0%") {
        double result = calculateFinalPrice("150", "0");
        REQUIRE(result == 150);
    }

    SECTION("should return zero when the discount is 100%") {
        double result = calculateFinalPrice("100", "100");
        REQUIRE(result == 0);
    }
}