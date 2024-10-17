#include <catch2/catch_test_macros.hpp>
#include <cstdint>

TEST_CASE("Test Compute Output Index", "[compute_output_index]") {
    SECTION("Test with two standard positive integers") {
        uint64_t idx_1 = 3;  // binary: 11
        uint64_t idx_2 = 5;  // binary: 101
        uint64_t expected = 6;  // 3 XOR 5 = 6
        uint64_t result = compute_output_index(idx_1, idx_2);
        REQUIRE(result == expected);
    }

    SECTION("Test with identical indices (should return 0)") {
        uint64_t idx_1 = 7;  // binary: 111
        uint64_t idx_2 = 7;  // binary: 111
        uint64_t expected = 0;  // 7 XOR 7 = 0
        uint64_t result = compute_output_index(idx_1, idx_2);
        REQUIRE(result == expected);
    }

    SECTION("Test with one index as zero") {
        uint64_t idx_1 = 0;  // binary: 0
        uint64_t idx_2 = 5;  // binary: 101
        uint64_t expected = 5;  // 0 XOR 5 = 5
        uint64_t result = compute_output_index(idx_1, idx_2);
        REQUIRE(result == expected);
    }

    SECTION("Test with large integer values") {
        uint64_t idx_1 = 1024;  // binary: 10000000000
        uint64_t idx_2 = 2048;  // binary: 100000000000
        uint64_t expected = 3072;  // 1024 XOR 2048 = 3072
        uint64_t result = compute_output_index(idx_1, idx_2);
        REQUIRE(result == expected);
    }
}