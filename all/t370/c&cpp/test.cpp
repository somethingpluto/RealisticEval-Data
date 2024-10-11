TEST_CASE("decompose function", "[decompose]") {
    // Test with valid input
    SECTION("Valid input") {
        auto result = decompose(5, std::make_tuple(3, 4));
        REQUIRE(result == std::make_tuple(1, 1));

        result = decompose(7, std::make_tuple(2, 4));
        REQUIRE(result == std::make_tuple(1, 3));
    }

    // Test with invalid input
    SECTION("Invalid input") {
        REQUIRE_THROWS(decompose(-1, std::make_tuple(3, 4)));
        REQUIRE_THROWS(decompose(12, std::make_tuple(3, 4)));

        REQUIRE_THROWS(decompose(5, std::make_tuple(2, 4)));
    }
}