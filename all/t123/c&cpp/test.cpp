#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>
#include <stdexcept>

std::vector<double> scaleToRange(const std::vector<double>& inputArray, double inputMin, double inputMax, double outputMin, double outputMax);

TEST_CASE("scaleToRange function tests") {
    SECTION("simple scaling") {
        auto result = scaleToRange({1, 2, 3, 4, 5}, 1, 5, 10, 50);
        REQUIRE(result == std::vector<double>({10, 20, 30, 40, 50}));
    }

    SECTION("scaling with negative input range") {
        auto result = scaleToRange({-5, 0, 5}, -5, 5, 0, 100);
        REQUIRE(result == std::vector<double>({0, 50, 100}));
    }

    SECTION("scaling with negative output range") {
        auto result = scaleToRange({0, 50, 100}, 0, 100, -100, 100);
        REQUIRE(result == std::vector<double>({-100, 0, 100}));
    }

    SECTION("input array containing the same value") {
        auto result = scaleToRange({2, 2, 2}, 1, 3, 0, 10);
        REQUIRE(result == std::vector<double>({5, 5, 5}));
    }

    SECTION("input value out of range should throw an error") {
        REQUIRE_THROWS_AS(scaleToRange({1, 2, 3, 6}, 1, 5, 0, 10), std::invalid_argument);
    }
}