TEST_CASE("elementsBeforeNull") {
    SECTION("returns elements before the first null") {
        std::vector<std::string> inputArray = {"element1", "element2", "", "element3", "element4"};
        auto result = elementsBeforeNull(inputArray);
        REQUIRE(result == std::vector<std::string>{"element1", "element2"});
    }

    SECTION("returns an empty array when input is empty") {
        std::vector<std::string> inputArray = {};
        auto result = elementsBeforeNull(inputArray);
        REQUIRE(result == std::vector<std::string>{});
    }

    SECTION("returns the same array if there is no null") {
        std::vector<std::string> inputArray = {"element1", "element2", "element3"};
        auto result = elementsBeforeNull(inputArray);
        REQUIRE(result == std::vector<std::string>{"element1", "element2", "element3"});
    }

    SECTION("returns an empty array if the first element is null") {
        std::vector<std::string> inputArray = {"", "element2", "element3"};
        auto result = elementsBeforeNull(inputArray);
        REQUIRE(result == std::vector<std::string>{});
    }

    SECTION("handles mixed types with null") {
        std::vector<std::variant<int, std::string, bool>> inputArray = {1, "text", std::monostate{}, true, false};
        auto result = elementsBeforeNull(inputArray);
        REQUIRE(result == std::vector<std::variant<int, std::string, bool>>{1, "text"});
    }

    SECTION("handles an array with only null") {
        std::vector<std::string> inputArray = {""};
        auto result = elementsBeforeNull(inputArray);
        REQUIRE(result == std::vector<std::string>{});
    }
}