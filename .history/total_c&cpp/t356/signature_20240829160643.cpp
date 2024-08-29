TEST_CASE("Sort Test Cases", "[Sort]") {
    // Test Case 1: Sorting an already sorted array
    vector<int> arr1 = {1, 2, 3, 4, 5};
    Sort(arr1);
    REQUIRE(arr1 == vector<int>{1, 2, 3, 4, 5});

    // Test Case 2: Sorting a reverse sorted array
    vector<int> arr2 = {5, 4, 3, 2, 1};
    Sort(arr2);
    REQUIRE(arr2 == vector<int>{1, 2, 3, 4, 5});

    // Test Case 3: Sorting an array with duplicate elements
    vector<int> arr3 = {3, 1, 2, 3, 2};
    Sort(arr3);
    REQUIRE(arr3 == vector<int>{1, 2, 2, 3, 3});

    // Test Case 4: Sorting an array with a single element
    vector<int> arr4 = {1};
    Sort(arr4);
    REQUIRE(arr4 == vector<int>{1});

    // Test Case 5: Sorting an empty array
    vector<int> arr5 = {};
    Sort(arr5);
    REQUIRE(arr5 == vector<int>{});
}