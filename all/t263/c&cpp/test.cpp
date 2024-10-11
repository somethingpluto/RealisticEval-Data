TEST_CASE("MatrixTraversal::spiral_traversal", "[MatrixTraversal]") {
    MatrixTraversal mt;

    SECTION("Empty matrix") {
        std::vector<std::vector<int>> matrix = {};
        REQUIRE(mt.spiral_traversal(matrix).empty());
    }

    SECTION("1x1 matrix") {
        std::vector<std::vector<int>> matrix = {{1}};
        std::vector<int> expected = {1};
        REQUIRE(mt.spiral_traversal(matrix) == expected);
    }

    SECTION("2x3 matrix") {
        std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}};
        std::vector<int> expected = {1, 2, 3, 6, 5, 4};
        REQUIRE(mt.spiral_traversal(matrix) == expected);
    }

    SECTION("3x2 matrix") {
        std::vector<std::vector<int>> matrix = {{1, 2}, {3, 4}, {5, 6}};
        std::vector<int> expected = {1, 2, 4, 6, 5, 3};
        REQUIRE(mt.spiral_traversal(matrix) == expected);
    }

    SECTION("4x4 matrix") {
        std::vector<std::vector<int>> matrix = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},
            {13, 14, 15, 16}
        };
        std::vector<int> expected = {1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10};
        REQUIRE(mt.spiral_traversal(matrix) == expected);
    }
}