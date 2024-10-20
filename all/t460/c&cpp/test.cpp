TEST_CASE("TestMatrixVectorMultiplication", "[matrix_vector_multiplication]") {
    SECTION("test_non_square_matrix") {
        std::vector<std::vector<float>> matrix = {{1, 2}, {3, 4}, {5, 6}};
        std::vector<float> vector = {2, 3};
        std::vector<float> expected_result = {8.0f, 18.0f, 28.0f};

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }

    SECTION("test_zero_vector") {
        std::vector<std::vector<float>> matrix = {{1, 2, 3}, {4, 5, 6}};
        std::vector<float> vector = {0, 0, 0};
        std::vector<float> expected_result = {0.0f, 0.0f};

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }

    SECTION("test_single_element") {
        std::vector<std::vector<float>> matrix = {{5}};
        std::vector<float> vector = {3};
        std::vector<float> expected_result = {15.0f};

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected_result);
    }

    SECTION("test_single_element_matrix_and_vector") {
        std::vector<std::vector<float>> matrix = {{3}};
        std::vector<float> vector = {4};
        std::vector<float> expected = {12.0f};

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected);
    }

    SECTION("test_compatible_sizes") {
        std::vector<std::vector<float>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        std::vector<float> vector = {1, 1, 1};
        std::vector<float> expected = {6.0f, 15.0f, 24.0f};

        REQUIRE(matrix_vector_multiplication(matrix, vector) == expected);
    }
}