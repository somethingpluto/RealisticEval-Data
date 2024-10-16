TEST_CASE("isSnakeCase") {
    SECTION("should return true for a valid snake_case string") {
        REQUIRE(isSnakeCase("snake_case") == true);
    }

    SECTION("should return true for a valid snake_case string with multiple words") {
        REQUIRE(isSnakeCase("snake_case_example") == true);
    }

    SECTION("should return false for a string that starts with an uppercase letter") {
        REQUIRE(isSnakeCase("Snake_Case") == false);
    }

    SECTION("should return false for a string with mixed case letters") {
        REQUIRE(isSnakeCase("snakeCASE") == false);
    }

    SECTION("should return false for a string with numbers") {
        REQUIRE(isSnakeCase("snake_case_123") == false);
    }

    SECTION("should return false for an empty string") {
        REQUIRE(isSnakeCase("") == false);
    }
}