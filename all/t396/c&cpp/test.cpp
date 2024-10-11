TEST_CASE("Test Length of Longest Increasing Subsequence", "[LIS]") {
    REQUIRE(length_of_LIS({10, 9, 2, 5, 3, 7, 101, 18}) == 4); // The longest increasing subsequence is [2, 3, 7, 101]
    REQUIRE(length_of_LIS({0, 1, 0, 3, 2, 3}) == 4);          // The longest increasing subsequence is [0, 1, 2, 3]
    REQUIRE(length_of_LIS({7, 7, 7, 7, 7, 7, 7}) == 1);       // All elements are equal, so the longest increasing subsequence has length 1
    REQUIRE(length_of_LIS({}) == 0);                           // Empty input should return 0
}