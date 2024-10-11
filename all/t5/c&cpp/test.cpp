TEST_CASE("Matrix multiplication tests") {

    SECTION("Test multiply") {
        std::vector<std::vector<int>> matrixA = {{1, 2}, {3, 4}};
        std::vector<std::vector<int>> matrixB = {{5, 6}, {7, 8}};
        std::vector<std::vector<int>> expected = {{19, 22}, {43, 50}};
        REQUIRE(matrix_multiply(matrixA, matrixB) == expected);
    }

    SECTION("Test empty matrix") {
        std::vector<std::vector<int>> matrixA = {};
        std::vector<std::vector<int>> matrixB = {};
        std::vector<std::vector<int>> expected = {};
        REQUIRE(matrix_multiply(matrixA, matrixB) == expected);
    }

    SECTION("Test compatible matrices") {
        std::vector<std::vector<int>> matrixA = {{1, 2, 3}, {4, 5, 6}};
        std::vector<std::vector<int>> matrixB = {{7, 8}, {9, 10}, {11, 12}};
        std::vector<std::vector<int>> expected = {{58, 64}, {139, 154}};
        REQUIRE(matrix_multiply(matrixA, matrixB) == expected);
    }
}