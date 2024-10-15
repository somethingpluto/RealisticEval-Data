TEST_CASE("countLetterChanges", "[countLetterChanges]") {
    SECTION("should count consecutive letters correctly") {
        auto result = countLetterChanges("aaabbcdeee");
        REQUIRE(result == std::vector<int>{3, 2, 1, 1, 3});
    }

    SECTION("should return an array with one count for a single character") {
        auto result = countLetterChanges("a");
        REQUIRE(result == std::vector<int>{1});
    }

    SECTION("should return counts for a string with no consecutive letters") {
        auto result = countLetterChanges("abcdef");
        REQUIRE(result == std::vector<int>{1, 1, 1, 1, 1, 1});
    }

    SECTION("should handle a string with only identical letters") {
        auto result = countLetterChanges("rrrrrr");
        REQUIRE(result == std::vector<int>{6});
    }

    SECTION("should handle a long string with random letters") {
        auto result = countLetterChanges("xxxyyyzzzaaaab");
        REQUIRE(result == std::vector<int>{3, 3, 3, 4, 1});
    }

    SECTION("should handle numeric characters in the string") {
        auto result = countLetterChanges("1122334455");
        REQUIRE(result == std::vector<int>{2, 2, 2, 2, 2});
    }
}