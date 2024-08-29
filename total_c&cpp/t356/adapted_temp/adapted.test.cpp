#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
TEST_CASE("BubbleSort Test Cases", "[bubbleSort]") {
    // Test Case 1: Sorting an already sorted array
    vector<int> arr1 = {1, 2, 3, 4, 5};
    bubbleSort(arr1);
    REQUIRE(arr1 == vector<int>{1, 2, 3, 4, 5});

    // Test Case 2: Sorting a reverse sorted array
    vector<int> arr2 = {5, 4, 3, 2, 1};
    bubbleSort(arr2);
    REQUIRE(arr2 == vector<int>{1, 2, 3, 4, 5});

    // Test Case 3: Sorting an array with duplicate elements
    vector<int> arr3 = {3, 1, 2, 3, 2};
    bubbleSort(arr3);
    REQUIRE(arr3 == vector<int>{1, 2, 2, 3, 3});

    // Test Case 4: Sorting an array with a single element
    vector<int> arr4 = {1};
    bubbleSort(arr4);
    REQUIRE(arr4 == vector<int>{1});

    // Test Case 5: Sorting an empty array
    vector<int> arr5 = {};
    bubbleSort(arr5);
    REQUIRE(arr5 == vector<int>{});
}