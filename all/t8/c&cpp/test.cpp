TEST_CASE("Test perform_polynomial_decryption basic functionality", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(4, 5, {1, 2, 3, 4}, {5, 6, 7, 8}) == std::vector<int>{4, 4, 4, 4});
}

TEST_CASE("Test perform_polynomial_decryption with zero secret key", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(3, 7, {0, 0, 0}, {6, 13, 20}) == std::vector<int>{6, 6, 6});
}

TEST_CASE("Test perform_polynomial_decryption with zero ciphertext", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(3, 9, {1, 2, 3}, {0, 0, 0}) == std::vector<int>{8, 7, 6});
}

TEST_CASE("Test perform_polynomial_decryption with large values", "[decryption]") {
    REQUIRE(perform_polynomial_decryption(2, 1000, {500, 500}, {1000, 1000}) == std::vector<int>{500, 500});
}