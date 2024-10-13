TEST_CASE("Test Matrix Multiplication", "[matrix_multiply]") {
    SECTION("Standard Matrices") {
        std::vector<std::vector<int>> mat1 = {{1, 2}, {3, 4}};
        std::vector<std::vector<int>> mat2 = {{5, 6}, {7, 8}};
        std::vector<std::vector<int>> expected = {{19, 22}, {43, 50}};
        
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }

    SECTION("Identity Matrix") {
        std::vector<std::vector<int>> mat1 = {{1, 0}, {0, 1}};
        std::vector<std::vector<int>> mat2 = {{5, 6}, {7, 8}};
        std::vector<std::vector<int>> expected = {{5, 6}, {7, 8}};
        
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }

    SECTION("Zero Matrix") {
        std::vector<std::vector<int>> mat1 = {{0, 0}, {0, 0}};
        std::vector<std::vector<int>> mat2 = {{5, 6}, {7, 8}};
        std::vector<std::vector<int>> expected = {{0, 0}, {0, 0}};
        
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }

    SECTION("Square Matrix Multiplication") {
        std::vector<std::vector<int>> mat1 = {{1, 2}, {3, 4}};
        std::vector<std::vector<int>> mat2 = {{5, 6}, {7, 8}};
        std::vector<std::vector<int>> expected = {{19, 22}, {43, 50}};
        
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }

    SECTION("Large Identity Matrix") {
        std::vector<std::vector<int>> mat1 = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        std::vector<std::vector<int>> mat2 = {{5, 6, 7}, {8, 9, 10}, {11, 12, 13}};
        std::vector<std::vector<int>> expected = {{5, 6, 7}, {8, 9, 10}, {11, 12, 13}};
        
        REQUIRE(matrix_multiply(mat1, mat2) == expected);
    }
}