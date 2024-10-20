TEST_CASE("Test longest non-decreasing subsequence") {
    SECTION("Non-decreasing sequence") {
        std::vector<int> nums = {5, 7, 4, 8, 6, 10, 2, 11};
        std::vector<int> expected = {5, 7, 8, 10, 11};
        REQUIRE(expected == find_longest_non_decreasing_subsequence(nums));
    }

    SECTION("All increasing") {
        std::vector<int> nums = {1, 2, 3, 4, 5};
        std::vector<int> expected = {1, 2, 3, 4, 5};
        REQUIRE(expected == find_longest_non_decreasing_subsequence(nums));
    }

    SECTION("All decreasing") {
        std::vector<int> nums = {5, 4, 3, 2, 1};
        std::vector<int> expected = {5};
        REQUIRE(expected == find_longest_non_decreasing_subsequence(nums));
    }

    SECTION("Single element") {
        std::vector<int> nums = {10};
        std::vector<int> expected = {10};
        REQUIRE(expected == find_longest_non_decreasing_subsequence(nums));
    }

    SECTION("Empty array") {
        std::vector<int> nums = {};
        std::vector<int> expected = {};
        REQUIRE(expected == find_longest_non_decreasing_subsequence(nums));
    }
}