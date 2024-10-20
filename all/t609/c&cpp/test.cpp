TEST_CASE("TestAnswer") {
    SECTION("Valid pair") {
        std::vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        std::vector<int> expected = {0, 1};  // 2 + 7 = 9
        REQUIRE(two_sum(nums, target) == expected);
    }

    SECTION("Negative numbers") {
        std::vector<int> nums = {-1, -2, -3, -4, -5};
        int target = -8;
        std::vector<int> expected = {2, 4};  // -3 + -5 = -8
        REQUIRE(two_sum(nums, target) == expected);
    }

    SECTION("Zero sum") {
        std::vector<int> nums = {0, 4, 3, 0};
        int target = 0;
        std::vector<int> expected = {0, 3};  // 0 + 0 = 0
        REQUIRE(two_sum(nums, target) == expected);
    }

    SECTION("No solution") {
        std::vector<int> nums = {1, 2, 3, 4, 5};
        int target = 10;
        REQUIRE_THROWS_AS(two_sum(nums, target), std::invalid_argument);
    }

    SECTION("Same number twice") {
        std::vector<int> nums = {3, 3};
        int target = 6;
        std::vector<int> expected = {0, 1};  // 3 + 3 = 6
        REQUIRE(two_sum(nums, target) == expected);
    }

    SECTION("Large numbers") {
        std::vector<int> nums = {2147483647, -2147483648, 0, 1};
        int target = 1;
        std::vector<int> expected = {2, 3};  // 0 + 1 = 1
        REQUIRE(two_sum(nums, target) == expected);
    }
}