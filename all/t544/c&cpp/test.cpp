TEST_CASE("filterOutEvenNumbers") {
    SECTION("removes all even numbers from the array") {
        std::vector<int> inputArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        std::vector<int> result = filterOutEvenNumbers(inputArray);
        REQUIRE(result == std::vector<int>{1, 3, 5, 7, 9});
    }

    SECTION("returns an empty array when input is empty") {
        std::vector<int> inputArray = {};
        std::vector<int> result = filterOutEvenNumbers(inputArray);
        REQUIRE(result == std::vector<int>{});
    }

    SECTION("returns the same array if all numbers are odd") {
        std::vector<int> inputArray = {1, 3, 5, 7, 9};
        std::vector<int> result = filterOutEvenNumbers(inputArray);
        REQUIRE(result == std::vector<int>{1, 3, 5, 7, 9});
    }

    SECTION("returns an empty array if all numbers are even") {
        std::vector<int> inputArray = {2, 4, 6, 8, 10};
        std::vector<int> result = filterOutEvenNumbers(inputArray);
        REQUIRE(result == std::vector<int>{});
    }

    SECTION("handles mixed positive and negative numbers") {
        std::vector<int> inputArray = {-3, -2, -1, 0, 1, 2, 3};
        std::vector<int> result = filterOutEvenNumbers(inputArray);
        REQUIRE(result == std::vector<int>{-3, -1, 1, 3});
    }

    SECTION("handles large numbers and zero correctly") {
        std::vector<int> inputArray = {0, 1000000000, 1000000001, 1000000002, 1000000003};
        std::vector<int> result = filterOutEvenNumbers(inputArray);
        REQUIRE(result == std::vector<int>{1000000001, 1000000003});
    }
}