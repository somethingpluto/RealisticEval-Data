TEST_CASE("Insertion Sort Tests", "[insertion_sort]") {
    SECTION("Basic unsorted array") {
        std::vector<float> arr = {12.4f, 11.2f, 13.5f, 5.6f, 6.7f};
        std::vector<float> expected = {5.6f, 6.7f, 11.2f, 12.4f, 13.5f};
        insertion_sort(arr);
        REQUIRE(arr == expected);
    }

    SECTION("Already sorted array") {
        std::vector<float> arr = {1.1f, 2.2f, 3.3f, 4.4f, 5.5f};
        std::vector<float> expected = {1.1f, 2.2f, 3.3f, 4.4f, 5.5f};
        insertion_sort(arr);
        REQUIRE(arr == expected);
    }

    SECTION("Reverse sorted array") {
        std::vector<float> arr = {5.5f, 4.4f, 3.3f, 2.2f, 1.1f};
        std::vector<float> expected = {1.1f, 2.2f, 3.3f, 4.4f, 5.5f};
        insertion_sort(arr);
        REQUIRE(arr == expected);
    }

    SECTION("Empty array") {
        std::vector<float> arr = {};
        std::vector<float> expected = {};
        insertion_sort(arr);
        REQUIRE(arr == expected);
    }

    SECTION("Single element array") {
        std::vector<float> arr = {3.3f};
        std::vector<float> expected = {3.3f};
        insertion_sort(arr);
        REQUIRE(arr == expected);
    }

    SECTION("Array with duplicate values") {
        std::vector<float> arr = {2.2f, 3.3f, 2.2f, 1.1f, 3.3f};
        std::vector<float> expected = {1.1f, 2.2f, 2.2f, 3.3f, 3.3f};
        insertion_sort(arr);
        REQUIRE(arr == expected);
    }

    SECTION("Large numbers") {
        std::vector<float> arr = {1e10f, 1e9f, 1e11f, 1e8f};
        std::vector<float> expected = {1e8f, 1e9f, 1e10f, 1e11f};
        insertion_sort(arr);
        REQUIRE(arr == expected);
    }
}