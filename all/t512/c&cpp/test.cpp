#include <catch2/catch_test_macros.hpp>
#include <vector>

TEST_CASE("Test convert_to_ring_format", "[convert_to_ring_format]") {
    SECTION("Test with no holes provided") {
        std::vector<int> holes = {};
        std::vector<int> expected(32, 1);  // All positions should be 1
        auto result = convert_to_ring_format(holes);
        REQUIRE(result == expected);
    }

    SECTION("Test with a single hole position") {
        std::vector<int> holes = {5};
        std::vector<int> expected(32, 1);
        expected[5] = 0;  // Only position 5 should be 0
        auto result = convert_to_ring_format(holes);
        REQUIRE(result == expected);
    }

    SECTION("Test with multiple hole positions") {
        std::vector<int> holes = {0, 2, 4, 8, 16};
        std::vector<int> expected(32, 1);
        for (int hole : holes) {
            expected[hole] = 0;  // Set specified positions to 0
        }
        auto result = convert_to_ring_format(holes);
        REQUIRE(result == expected);
    }

    SECTION("Test with some hole positions out of bounds") {
        std::vector<int> holes = {-1, 32, 5, 10};  // -1 and 32 are out of bounds
        std::vector<int> expected(32, 1);
        expected[5] = 0;  // Only position 5 and 10 should be 0
        expected[10] = 0;
        auto result = convert_to_ring_format(holes);
        REQUIRE(result == expected);
    }

    SECTION("Test with all positions as holes") {
        std::vector<int> holes;
        for (int i = 0; i < 32; ++i) {
            holes.push_back(i);
        }
        std::vector<int> expected(32, 0);  // All positions should be 0
        auto result = convert_to_ring_format(holes);
        REQUIRE(result == expected);
    }
}