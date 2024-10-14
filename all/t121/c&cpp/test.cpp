#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>

// Function prototype
std::vector<int> adjustArrayLength(int targetLength, const std::vector<int>& array);

TEST_CASE("adjustArrayLength function tests") {
    SECTION("Array length equal to the target length") {
        auto result = adjustArrayLength(5, {1, 2, 3, 4, 5});
        REQUIRE(result == std::vector<int>{1, 2, 3, 4, 5});
    }

    SECTION("Array length shorter than the target length") {
        auto result = adjustArrayLength(8, {1, 2, 3});
        REQUIRE(result == std::vector<int>{1, 2, 3, 1, 2, 3, 1, 2});
    }

    SECTION("Array length shorter than the target length, target length is a multiple of array length") {
        auto result = adjustArrayLength(6, {10, 20});
        REQUIRE(result == std::vector<int>{10, 20, 10, 20, 10, 20});
    }

    SECTION("Array length shorter than the target length, target length is not a multiple of array length") {
        auto result = adjustArrayLength(7, {7, 14, 21});
        REQUIRE(result == std::vector<int>{7, 14, 21, 7, 14, 21, 7});
    }
}