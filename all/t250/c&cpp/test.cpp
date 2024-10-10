TEST_CASE("Invert Dictionary", "[invertDictionary]") {
    // Test case 1
    std::unordered_map<int, int> dict1 = {{1, 2}, {3, 4}};
    std::unordered_map<int, std::vector<int>> expected1 = {{2, {1}}, {4, {3}}};
    REQUIRE(invertDictionary(dict1) == expected1);

    // Test case 2
    std::unordered_map<int, int> dict2 = {{5, 6}, {7, 8}, {9, 6}};
    std::unordered_map<int, std::vector<int>> expected2 = {{6, {5, 9}}, {8, {7}}};
    REQUIRE(invertDictionary(dict2) == expected2);

    // Test case 3
    std::unordered_map<int, int> dict3 = {};
    std::unordered_map<int, std::vector<int>> expected3 = {};
    REQUIRE(invertDictionary(dict3) == expected3);
}