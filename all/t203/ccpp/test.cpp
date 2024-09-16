TEST_CASE("Test reverseRange function") {
    SECTION("Reverse entire vector") {
        std::vector<int> v = {1, 2, 3, 4, 5};
        reverseRange(v, 0, 4);
        std::vector<int> expected = {5, 4, 3, 2, 1};
        REQUIRE(v == expected);
    }

    SECTION("Reverse subrange in the middle") {
        std::vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8};
        reverseRange(v, 2, 5);
        std::vector<int> expected = {1, 2, 6, 5, 4, 3, 7, 8};
        REQUIRE(v == expected);
    }

    SECTION("Reverse a single element range") {
        std::vector<int> v = {1, 2, 3, 4, 5};
        reverseRange(v, 2, 2);
        std::vector<int> expected = {1, 2, 3, 4, 5};
        REQUIRE(v == expected);
    }

    SECTION("Reverse range with invalid indices") {
        std::vector<int> v = {1, 2, 3, 4, 5};
        reverseRange(v, -1, 3);  // Invalid start index
        std::vector<int> expected = {1, 2, 3, 4, 5}; // No change
        REQUIRE(v == expected);
    }

    SECTION("Reverse range at the end of the vector") {
        std::vector<int> v = {1, 2, 3, 4, 5, 6};
        reverseRange(v, 3, 5);
        std::vector<int> expected = {1, 2, 3, 6, 5, 4};
        REQUIRE(v == expected);
    }
}