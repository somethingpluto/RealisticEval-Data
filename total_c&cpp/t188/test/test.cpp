
bool isSorted(const std::vector<int>& arr) {
    for (size_t i = 1; i < arr.size(); ++i) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

TEST_CASE("Shell sort - Basic functionality", "[shellSort]") {
    SECTION("Test Case 1: Already sorted array") {
        std::vector<int> arr = {1, 2, 3, 4, 5};
        shellSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Test Case 2: Reverse sorted array") {
        std::vector<int> arr = {5, 4, 3, 2, 1};
        shellSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Test Case 3: Array with duplicate elements") {
        std::vector<int> arr = {4, 2, 2, 4, 1};
        shellSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Test Case 4: Array with negative numbers") {
        std::vector<int> arr = {-3, -1, -4, -2, 0};
        shellSort(arr);
        REQUIRE(isSorted(arr) == true);
    }

    SECTION("Test Case 5: Empty array") {
        std::vector<int> arr = {};
        shellSort(arr);
        REQUIRE(isSorted(arr) == true);
    }
}