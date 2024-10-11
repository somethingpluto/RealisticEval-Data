TEST_CASE("Test Length of Longest Increasing Subsequence", "[length_of_LIS]") {
    SECTION("Example 1") {
        std::vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
        REQUIRE(length_of_LIS(nums) == 4);
    }

    SECTION("Example 2") {
        std::vector<int> nums = {0, 1, 0, 3, 2, 3};
        REQUIRE(length_of_LIS(nums) == 4);
    }

    SECTION("Example 3") {
        std::vector<int> nums = {7, 7, 7, 7, 7, 7, 7};
        REQUIRE(length_of_LIS(nums) == 1);
    }

    SECTION("Empty Input") {
        std::vector<int> nums = {};
        REQUIRE(length_of_LIS(nums) == 0);
    }
}