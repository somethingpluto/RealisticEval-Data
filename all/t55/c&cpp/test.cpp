TEST_CASE("min_removals_to_make_unique", "[min_removals_to_make_unique]") {
    std::vector<int> nums = {3, 3, 1, 2, 2, 1};
    REQUIRE(min_removals_to_make_unique(nums) == 3);

    nums = {4, 5, 6, 7, 8};
    REQUIRE(min_removals_to_make_unique(nums) == 0);

    nums = {1, 1, 1, 1, 1};
    REQUIRE(min_removals_to_make_unique(nums) == 4);
}