TEST_CASE("Test inversion of a dictionary without duplicate values") {
    std::unordered_map<std::string, std::string> originalDict = {{"a", "1"}, {"b", "2"}, {"c", "3"}};
    std::unordered_map<std::string, std::string> expected = {{"1", "a"}, {"2", "b"}, {"3", "c"}};
    auto result = invert_dictionary(originalDict);

    REQUIRE(result == expected);
}

TEST_CASE("Test inversion of a dictionary with duplicate values") {
    std::unordered_map<std::string, std::string> originalDict = {{"a", "1"}, {"b", "1"}, {"c", "2"}};
    std::unordered_map<std::string, std::vector<std::string>> expected = {{"1", {"a", "b"}}, {"2", {"c"}}};
    auto result = invert_dictionary(originalDict);

    REQUIRE(result == expected);
}

TEST_CASE("Test inversion of an empty dictionary") {
    std::unordered_map<std::string, std::string> originalDict = {};
    std::unordered_map<std::string, std::vector<std::string>> expected = {};
    auto result = invert_dictionary(originalDict);

    REQUIRE(result == expected);
}

TEST_CASE("Test inversion of a dictionary with non-string keys") {
    // Note: In C++, all keys and values are strings for simplicity.
    std::unordered_map<std::string, std::string> originalDict = {{"1", "apple"}, {"2", "banana"}, {"3", "apple"}};
    std::unordered_map<std::string, std::vector<std::string>> expected = {{"apple", {"1", "3"}}, {"banana", {"2"}}};
    auto result = invert_dictionary(originalDict);

    REQUIRE(result == expected);
}

TEST_CASE("Test inversion of a dictionary with mixed key and value types") {
    // Note: In C++, all keys and values are strings for simplicity.
    std::unordered_map<std::string, std::string> originalDict = {{"a", "1"}, {"2", "two"}, {"three", "3"}};
    std::unordered_map<std::string, std::vector<std::string>> expected = {{"1", {"a"}}, {"two", {"2"}}, {"3", {"three"}}};
    auto result = invert_dictionary(originalDict);

    REQUIRE(result == expected);
}