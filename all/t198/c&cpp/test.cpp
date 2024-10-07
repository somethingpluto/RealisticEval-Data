TEST_CASE("General case", "[findMaxDifference]") {
    std::vector<int> l = {2, 3, 10, 6, 4, 8, 1};
    REQUIRE(findMaxDifference(l) == 8);  // Maximum difference is 10 - 2 = 8
}

// Test case 2: Decreasing sequence
TEST_CASE("Decreasing sequence", "[findMaxDifference]") {
    std::vector<int> l = {10, 9, 8, 7, 6, 5};
    REQUIRE(findMaxDifference(l) == 0);  // Maximum difference should be 0, as all differences are negative
}

// Test case 3: All elements the same
TEST_CASE("All elements the same", "[findMaxDifference]") {
    std::vector<int> l = {5, 5, 5, 5, 5};
    REQUIRE(findMaxDifference(l) == 0);  // Maximum difference is 5 - 5 = 0
}

// Test case 4: Only two elements
TEST_CASE("Only two elements", "[findMaxDifference]") {
    std::vector<int> l = {3, 8};
    REQUIRE(findMaxDifference(l) == 5);  // Maximum difference is 8 - 3 = 5
}

// Test case 5: Only one element
TEST_CASE("Single element", "[findMaxDifference]") {
    std::vector<int> l = {4};
    REQUIRE(findMaxDifference(l) == 0);  // Only one element, no difference to calculate
}