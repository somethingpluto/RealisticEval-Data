TEST_CASE("Test numerical_str_convert function", "[numerical_str_convert]") {
    // Test case 1: Input is an integer
    REQUIRE(numerical_str_convert("42") == 42);

    // Test case 2: Input is a floating-point number
    REQUIRE(numerical_str_convert("3.14") == 3.14);

    // Test case 3: Input is a non-numeric string
    REQUIRE(numerical_str_convert("abc") == "abc");
}
