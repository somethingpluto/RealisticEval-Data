TEST_CASE("Test getPalindromeList", "[palindrome]") {
    SECTION("Empty list for negative input") {
        std::vector<int> result = getPalindromeList(-1);
        REQUIRE(result.empty());
    }

    SECTION("Single element list for zero") {
        std::vector<int> result = getPalindromeList(0);
        REQUIRE(result.size() == 1);
        REQUIRE(result[0] == 0);
    }

    SECTION("Multiple elements list for positive input") {
        std::vector<int> result = getPalindromeList(100);
        std::vector<int> expected = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99};
        REQUIRE(result == expected);
    }

    SECTION("No palindromes in the middle of the range") {
        std::vector<int> result = getPalindromeList(12);
        std::vector<int> expected = {0, 1, 2, 11};
        REQUIRE(result == expected);
    }
}