TEST_CASE("filterArray") {
    // Qualification function that checks if a number is greater than 10
    auto isGreaterThanTen = [](int num) { return num > 10; };

    SECTION("filters out numbers less than or equal to 10") {
        std::vector<int> unfilteredArray = {5, 12, 3, 18, 7, 10, 15};
        auto result = filterArray(unfilteredArray, isGreaterThanTen);
        REQUIRE(result == std::vector<int>({12, 18, 15}));
    }

    SECTION("returns an empty array when all elements are disqualified") {
        std::vector<int> unfilteredArray = {1, 2, 3, 4, 5};
        auto result = filterArray(unfilteredArray, isGreaterThanTen);
        REQUIRE(result.empty());
    }

    SECTION("returns the same array when all elements are qualified") {
        std::vector<int> unfilteredArray = {11, 12, 15, 20};
        auto result = filterArray(unfilteredArray, isGreaterThanTen);
        REQUIRE(result == std::vector<int>({11, 12, 15, 20}));
    }

    SECTION("handles an empty array input") {
        std::vector<int> unfilteredArray = {};
        auto result = filterArray(unfilteredArray, isGreaterThanTen);
        REQUIRE(result.empty());
    }

    SECTION("filters out strings based on length") {
        auto isLongerThanThreeChars = [](const std::string& str) { return str.length() > 3; };
        std::vector<std::string> unfilteredArray = {"a", "ab", "abc", "abcd", "abcde"};
        auto result = filterArray(unfilteredArray, isLongerThanThreeChars);
        REQUIRE(result == std::vector<std::string>({"abcd", "abcde"}));
    }

    SECTION("correctly filters an array with mixed types") {
        auto isString = [](const std::variant<int, std::string, bool, std::nullptr_t>& item) {
            return std::holds_alternative<std::string>(item);
        };
        std::vector<std::variant<int, std::string, bool, std::nullptr_t>> unfilteredArray = {1, "hello", true, "world", nullptr};
        auto result = filterArray(unfilteredArray, isString);
        REQUIRE(result == std::vector<std::variant<int, std::string, bool, std::nullptr_t>>({"hello", "world"}));
    }

    SECTION("filters based on an object property") {
        auto hasValueGreaterThanFive = [](const std::map<std::string, int>& obj) { return obj.at("value") > 5; };
        std::vector<std::map<std::string, int>> unfilteredArray = {{{"value", 3}}, {{"value", 5}}, {{"value", 7}}};
        auto result = filterArray(unfilteredArray, hasValueGreaterThanFive);
        REQUIRE(result == std::vector<std::map<std::string, int>>({{{"value", 7}}}));
    }

    SECTION("returns an empty array when no qualifying function is provided") {
        std::vector<int> unfilteredArray = {1, 2, 3, 4, 5};
        auto result = filterArray(unfilteredArray, [](int) { return false; }); // Always returns false
        REQUIRE(result.empty());
    }
}