TEST_CASE("Test Matrix Power", "[matrix_power]") {
    SECTION("Identity Matrix") {
        // Testing the power function with an identity matrix
        std::vector<std::vector<int>> matrix = {{1, 0}, {0, 1}};
        std::vector<std::vector<int>> expected = {{1, 0}, {0, 1}};
        auto result = power(matrix, 1);
        REQUIRE(result == expected);
    }

    SECTION("Zero Power") {
        // Testing matrix to the power of zero (should return identity)
        std::vector<std::vector<int>> matrix = {{2, 3}, {1, 4}};
        std::vector<std::vector<int>> expected = {{1, 0}, {0, 1}};
        auto result = power(matrix, 0);
        REQUIRE(result == expected);
    }

    SECTION("Positive Power") {
        // Testing matrix to a positive power
        std::vector<std::vector<int>> matrix = {{2, 1}, {1, 3}};
        std::vector<std::vector<int>> expected = {{5, 5}, {5, 10}};  // This is the result of matrix^2
        auto result = power(matrix, 2);
        REQUIRE(result == expected);
    }

    SECTION("Negative Power") {
        // Testing matrix to a negative power (should throw std::invalid_argument)
        std::vector<std::vector<int>> matrix = {{2, 1}, {1, 3}};
        REQUIRE_THROWS_AS(power(matrix, -1), std::invalid_argument);
    }
}