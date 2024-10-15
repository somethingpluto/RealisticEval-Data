TEST_CASE("compareArrays") {
    SECTION("should return true for identical arrays with same order") {
        std::vector<int> arr1 = {1, 2, 3};
        std::vector<int> arr2 = {1, 2, 3};
        REQUIRE(compareArrays(arr1, arr2) == true);
    }

    SECTION("should return true for identical arrays with different order") {
        std::vector<int> arr1 = {3, 2, 1};
        std::vector<int> arr2 = {1, 2, 3};
        REQUIRE(compareArrays(arr1, arr2) == true);
    }

    SECTION("should return false for arrays with different elements") {
        std::vector<int> arr1 = {1, 2, 3};
        std::vector<int> arr2 = {4, 5, 6};
        REQUIRE(compareArrays(arr1, arr2) == false);
    }

    SECTION("should return false for arrays with different lengths") {
        std::vector<int> arr1 = {1, 2, 3};
        std::vector<int> arr2 = {1, 2};
        REQUIRE(compareArrays(arr1, arr2) == false);
    }

    SECTION("should return true for arrays with duplicate elements but same unique set") {
        std::vector<int> arr1 = {1, 1, 2, 3, 3};
        std::vector<int> arr2 = {3, 2, 1, 1};
        REQUIRE(compareArrays(arr1, arr2) == true);
    }
}