TEST_CASE("TestBinarySearchClosest") {

    SECTION("Target present") {
        // Test when the target is present in the array.
        std::vector<int> array = {1, 3, 5, 7, 9, 11};
        int target = 7;
        int result = binary_search_closest(array, target);
        REQUIRE(result == 3); // Target should be found at index 3.
    }

    SECTION("Closest element smaller") {
        // Test when the target is not present and the closest element is smaller.
        std::vector<int> array = {1, 3, 5, 7, 9, 11};
        int target = 6;
        int result = binary_search_closest(array, target);
        REQUIRE(result == 2); // Closest element should be 5 at index 2.
    }

    SECTION("Closest element larger") {
        // Test when the target is not present and the closest element is larger.
        std::vector<int> array = {1, 3, 5, 7, 9, 11};
        int target = 8;
        int result = binary_search_closest(array, target);
        REQUIRE(result == 3); // Closest element should be 7 at index 3.
    }

    SECTION("Target smaller than all") {
        // Test when the target is smaller than all elements in the array.
        std::vector<int> array = {1, 3, 5, 7, 9, 11};
        int target = 0;
        int result = binary_search_closest(array, target);
        REQUIRE(result == 0); // Closest element should be 1 at index 0.
    }

    SECTION("Target larger than all") {
        // Test when the target is larger than all elements in the array.
        std::vector<int> array = {1, 3, 5, 7, 9, 11};
        int target = 12;
        int result = binary_search_closest(array, target);
        REQUIRE(result == 5); // Closest element should be 11 at index 5.
    }
}