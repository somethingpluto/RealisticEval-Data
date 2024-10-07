// Helper function to check if the array is sorted
bool isSorted(const std::vector<int>& arr) {
    for (size_t i = 1; i < arr.size(); ++i) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

// Test cases
TEST_CASE("Hill Sort") {
    SECTION("Sort an already sorted array") {
        std::vector<int> arr = {1, 2, 3, 4, 5};
        hillSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Sort an array in reverse order") {
        std::vector<int> arr = {5, 4, 3, 2, 1};
        hillSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Sort an array with duplicate values") {
        std::vector<int> arr = {3, 1, 2, 3, 2};
        hillSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Sort an array with all identical values") {
        std::vector<int> arr = {1, 1, 1, 1, 1};
        hillSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Sort an empty array") {
        std::vector<int> arr = {};
        hillSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Sort an array with one element") {
        std::vector<int> arr = {42};
        hillSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Sort a large random array") {
        std::vector<int> arr = {3, 7, 2, 5, 1, 4, 6, 0, 9, 8};
        hillSort(arr);
        REQUIRE(isSorted(arr) == true);
    }
}