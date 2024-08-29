#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../original.cpp"
TEST_CASE("sortNames Test Cases", "[sortNames]") {
    // Test Case 1: Simple case with different numbers
    vector<string> arr1 = {"Alice10", "Bob2", "Charlie7"};
    vector<string> expected1 = {"Bob2", "Charlie7", "Alice10"};
    REQUIRE(sortNames(arr1) == expected1);

    // Test Case 2: Same numbers, different names
    vector<string> arr2 = {"Alice10", "Charlie10", "Bob10"};
    vector<string> expected2 = {"Alice10", "Bob10", "Charlie10"};
    REQUIRE(sortNames(arr2) == expected2);

    // Test Case 3: Mixed case with different names and numbers
    vector<string> arr3 = {"Alice3", "Bob2", "Charlie3", "Bob1"};
    vector<string> expected3 = {"Bob1", "Bob2", "Alice3", "Charlie3"};
    REQUIRE(sortNames(arr3) == expected3);

    // Test Case 4: Single element
    vector<string> arr4 = {"Alice5"};
    vector<string> expected4 = {"Alice5"};
    REQUIRE(sortNames(arr4) == expected4);

    // Test Case 5: Empty array
    vector<string> arr5 = {};
    vector<string> expected5 = {};
    REQUIRE(sortNames(arr5) == expected5);
}