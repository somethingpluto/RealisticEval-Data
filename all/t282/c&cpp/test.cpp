TEST_CASE("Flatten Array", "[flattenArray]") {
    // Test Case 1
    std::vector<std::vector<int>> multiDimArray1 = {{1, 2, 3}, {4, 5}, {6}};
    std::vector<int> expected1 = {1, 2, 3, 4, 5, 6};
    REQUIRE(flattenArray(multiDimArray1) == expected1);

    // Test Case 2
    std::vector<std::vector<int>> multiDimArray2 = {};
    std::vector<int> expected2 = {};
    REQUIRE(flattenArray(multiDimArray2) == expected2);

    // Test Case 3
    std::vector<std::vector<int>> multiDimArray3 = {{7}, {}, {8, 9}};
    std::vector<int> expected3 = {7, 8, 9};
    REQUIRE(flattenArray(multiDimArray3) == expected3);

    // Test Case 4
    std::vector<std::vector<int>> multiDimArray4 = {{10, 11}, {12, 13, 14}, {15}};
    std::vector<int> expected4 = {10, 11, 12, 13, 14, 15};
    REQUIRE(flattenArray(multiDimArray4) == expected4);
}