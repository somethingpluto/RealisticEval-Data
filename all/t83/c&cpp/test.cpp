TEST_CASE("Test Rotate Vector Elements", "[rotate_vector_elements]") {
    SECTION("Basic Rotation") {
        REQUIRE(rotate_vector_elements({1, 2, 3, 4}) == std::vector<int>({2, 3, 4, 1}));
    }

    SECTION("Single Element List") {
        REQUIRE(rotate_vector_elements({10}) == std::vector<int>({10}));
    }

    SECTION("Empty List") {
        REQUIRE(rotate_vector_elements({}) == std::vector<int>({}));
    }

    SECTION("Two Element List") {
        REQUIRE(rotate_vector_elements({5, 9}) == std::vector<int>({9, 5}));
    }

    SECTION("Large List") {
        std::vector<int> large_list;
        for (int i = 1; i <= 1000; ++i) {
            large_list.push_back(i);
        }
        std::vector<int> rotated_list = rotate_vector_elements(large_list);
        std::vector<int> expected_list(large_list.begin() + 1, large_list.end());
        expected_list.push_back(large_list.front());

        REQUIRE(rotated_list == expected_list);
    }
}