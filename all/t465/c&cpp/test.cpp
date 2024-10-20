TEST_CASE("Test Matrix-Vector Multiplication", "[matrix-vector-multiplication]") {
    SECTION("Test with a simple 2x2 matrix and a 2-element vector") {
        std::vector<std::vector<double>> matrix = {{1, 2}, {3, 4}};
        std::vector<double> vector = {5, 6};
        std::vector<double> expected_result = {17, 39};  // [1*5 + 2*6, 3*5 + 4*6]

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }

    SECTION("Test with a 3x3 matrix and a 3-element vector") {
        std::vector<std::vector<double>> matrix = {{1, 0, 2}, {0, 1, 2}, {1, 1, 0}};
        std::vector<double> vector = {3, 4, 5};
        std::vector<double> expected_result = {13, 14, 7};  // [1*3 + 0*4 + 2*5, 0*3 + 1*4 + 2*5, 1*3 + 1*4 + 0*5]

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }

    SECTION("Test with a zero matrix and a vector") {
        std::vector<std::vector<double>> matrix = {{0, 0}, {0, 0}};
        std::vector<double> vector = {1, 1};
        std::vector<double> expected_result = {0, 0};  // Zero matrix multiplied by any vector yields zero

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }

    SECTION("Test with a matrix having negative values") {
        std::vector<std::vector<double>> matrix = {{-1, -2}, {-3, -4}};
        std::vector<double> vector = {1, 1};
        std::vector<double> expected_result = {-3, -7};  // [-1*1 + -2*1, -3*1 + -4*1]

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }

    SECTION("Test with non-square matrix (2x3) and a compatible vector (3-element)") {
        std::vector<std::vector<double>> matrix = {{1, 2, 3}, {4, 5, 6}};
        std::vector<double> vector = {1, 0, 1};
        std::vector<double> expected_result = {4, 10};  // [1*1 + 2*0 + 3*1, 4*1 + 5*0 + 6*1]

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }
}