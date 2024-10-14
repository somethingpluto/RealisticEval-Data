TEST_CASE("findMedian", "[median]") {
    // Example usage with a large array
    SECTION("should find the median of a large array with 10001 random elements") {
        std::vector<int> largeArray(10001);
        std::generate(largeArray.begin(), largeArray.end(), []() {
            return rand() % 10000; // Random number between 0 and 9999
        });
        double medianLargeArray = findMedian(largeArray);
        // Check if the result is a number (not NaN)
        REQUIRE(!std::isnan(medianLargeArray));
    }

    // Test Case 1: Odd number of elements
    SECTION("should return 3 for an array with odd number of elements") {
        std::vector<int> arr1 = {3, 1, 4, 1, 5, 9, 2};
        double median1 = findMedian(arr1);
        REQUIRE(median1 == 3);
    }

    // Test Case 2: Even number of elements
    SECTION("should return 6 for an array with even number of elements") {
        std::vector<int> arr2 = {10, 2, 3, 5, 7, 8};
        double median2 = findMedian(arr2);
        REQUIRE(median2 == 6);
    }

    // Test Case 3: Array with duplicate elements
    SECTION("should return 2 for an array with duplicate elements") {
        std::vector<int> arr3 = {1, 2, 2, 2, 3};
        double median3 = findMedian(arr3);
        REQUIRE(median3 == 2);
    }

    // Test Case 4: Array with negative numbers
    SECTION("should return 0 for an array with negative and positive numbers") {
        std::vector<int> arr4 = {-5, -10, 0, 5, 10};
        double median4 = findMedian(arr4);
        REQUIRE(median4 == 0);
    }

    // Test Case 5: Array with a single element
    SECTION("should return the only element for an array with a single element") {
        std::vector<int> arr5 = {42};
        double median5 = findMedian(arr5);
        REQUIRE(median5 == 42);
    }
}