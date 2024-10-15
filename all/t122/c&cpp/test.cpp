#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>
#include <optional>

// Assuming safeSplice function is declared here

TEST_CASE("safeSplice", "[splice]") {
    SECTION("replaces removed elements with a new element") {
        std::vector<std::string> inputArray = {"a", "b", "c", "d", "e"};
        std::vector<std::string> expected = {"a", "z", "e"};
        REQUIRE(safeSplice(inputArray, 3, 1, "z") == expected);
    }

    SECTION("should remove specified elements and replace with new element") {
        std::vector<int> inputArray = {1, 2, 3, 4, 5};
        int amountToRemove = 2;
        int indexToRemove = 1;
        int replaceWith = 99;
        std::vector<int> result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        REQUIRE(result == std::vector<int>{1, 99, 4, 5});
    }

    SECTION("should handle removing elements from the end of the array") {
        std::vector<int> inputArray = {1, 2, 3, 4, 5};
        int amountToRemove = 2;
        int indexToRemove = 3;
        std::vector<int> result = safeSplice(inputArray, amountToRemove, indexToRemove);
        REQUIRE(result == std::vector<int>{1, 2, 3});
    }

    SECTION("should handle the case where no elements are removed") {
        std::vector<int> inputArray = {1, 2, 3, 4, 5};
        int amountToRemove = 0;
        int indexToRemove = 2;
        int replaceWith = 99;
        std::vector<int> result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        REQUIRE(result == std::vector<int>{1, 2, 99, 3, 4, 5});
    }

    SECTION("should handle edge case with an empty input array") {
        std::vector<int> inputArray = {};
        int amountToRemove = 1;
        int indexToRemove = 0;
        int replaceWith = 99;
        std::vector<int> result = safeSplice(inputArray, amountToRemove, indexToRemove, replaceWith);
        REQUIRE(result == std::vector<int>{99});
    }
}